#!/usr/bin/env python3
"""
Analyze GitHub project board and count open issues with "P0" label.

This script accesses the GitHub project board and counts how many open issues
have the "P0" label.
"""

import os
import sys
from typing import Optional
import requests
from github import Github


def get_github_token() -> Optional[str]:
    """Get GitHub token from environment variable."""
    token = os.getenv("GITHUB_TOKEN")
    if not token:
        print("Error: GITHUB_TOKEN environment variable is not set.")
        print("Please set it with: export GITHUB_TOKEN=your_token_here")
        print("\nTo create a token:")
        print("1. Go to https://github.com/settings/tokens")
        print("2. Generate a new token with 'repo', 'read:org', and 'read:project' permissions")
        sys.exit(1)
    return token


def count_p0_issues_rest_api(org_name: str, project_number: int) -> int:
    """
    Count P0 issues using REST API by searching all repositories in the org.
    
    This approach searches all repositories in the organization for open issues
    with the P0 label. Tries multiple label formats to catch variations.
    """
    token = get_github_token()
    g = Github(token)
    
    try:
        org = g.get_organization(org_name)
        p0_count = 0
        all_p0_issues = []
        
        print(f"Searching for open issues with 'P0' label in {org_name}...")
        
        # Try different label formats (P0, p0, etc.)
        label_variants = ["P0", "p0"]
        
        for label_variant in label_variants:
            try:
                # Search for issues with P0 label across the organization
                query = f"org:{org_name} is:issue is:open label:{label_variant}"
                print(f"  Searching with query: {query}")
                issues = g.search_issues(query)
                
                print(f"  Found {issues.totalCount} potential matches for label '{label_variant}'")
                
                # Collect all issues (handle pagination)
                for issue in issues:
                    # Check if issue actually has P0 label (case-insensitive)
                    issue_labels = [label.name for label in issue.labels]
                    has_p0 = any(label.upper() == "P0" for label in issue_labels)
                    
                    if has_p0:
                        # Avoid duplicates by checking repo + number
                        issue_id = (issue.repository.full_name, issue.number)
                        existing_ids = [(i.repository.full_name, i.number) for i in all_p0_issues]
                        if issue_id not in existing_ids:
                            all_p0_issues.append(issue)
                
            except Exception as e:
                print(f"  Warning: Search for label '{label_variant}' failed: {e}")
                continue
        
        p0_count = len(all_p0_issues)
        
        print(f"\nFound {p0_count} open issue(s) with 'P0' label")
        
        # List the issues
        if p0_count > 0:
            print("\nP0 Issues:")
            for issue in all_p0_issues[:20]:  # Show first 20
                repo_name = issue.repository.full_name
                print(f"  - {repo_name}#{issue.number}: {issue.title} ({issue.html_url})")
            if p0_count > 20:
                print(f"  ... and {p0_count - 20} more")
        else:
            print("\n⚠️  No P0 issues found. This might mean:")
            print("   - The label name is different (check case sensitivity)")
            print("   - Issues are in private repos and token lacks access")
            print("   - The search query needs adjustment")
        
        return p0_count
        
    except Exception as e:
        print(f"Error accessing GitHub API: {e}")
        raise


def count_p0_issues_graphql(org_name: str, project_number: int) -> int:
    """
    Count P0 issues using GraphQL API to access the project board directly.
    
    This approach uses GraphQL to query the project board directly.
    """
    token = get_github_token()
    
    # GraphQL query to get project items
    query = """
    query($org: String!, $projectNumber: Int!) {
      organization(login: $org) {
        projectV2(number: $projectNumber) {
          title
          items(first: 100) {
            nodes {
              content {
                ... on Issue {
                  number
                  title
                  state
                  labels(first: 10) {
                    nodes {
                      name
                    }
                  }
                }
              }
            }
          }
        }
      }
    }
    """
    
    variables = {
        "org": org_name,
        "projectNumber": project_number
    }
    
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json",
    }
    
    url = "https://api.github.com/graphql"
    
    try:
        response = requests.post(
            url,
            json={"query": query, "variables": variables},
            headers=headers
        )
        response.raise_for_status()
        
        data = response.json()
        
        if "errors" in data:
            errors = data['errors']
            error_messages = [err.get('message', '') for err in errors]
            
            # Check if it's a scope error by looking at error type
            has_scope_error = any(
                err.get('type') == 'INSUFFICIENT_SCOPES' or 
                'read:project' in err.get('message', '') 
                for err in errors
            )
            
            if has_scope_error:
                print(f"⚠️  GraphQL requires 'read:project' scope.")
                print(f"   Current token scopes are insufficient.")
                print(f"   Please add 'read:project' scope to your token at:")
                print(f"   https://github.com/settings/tokens")
                print(f"\n   Falling back to REST API search...")
                raise Exception("Insufficient scopes for GraphQL")
            else:
                print(f"GraphQL errors: {errors}")
                raise Exception(f"GraphQL query failed: {error_messages}")
        
        project = data.get("data", {}).get("organization", {}).get("projectV2")
        if not project:
            print(f"Project {project_number} not found or not accessible")
            return 0
        
        items = project.get("items", {}).get("nodes", [])
        p0_count = 0
        p0_issues = []
        
        for item in items:
            content = item.get("content")
            if content and content.get("__typename") == "Issue":
                state = content.get("state")
                labels = content.get("labels", {}).get("nodes", [])
                label_names = [label.get("name") for label in labels]
                
                if state == "OPEN" and "P0" in label_names:
                    p0_count += 1
                    p0_issues.append({
                        "number": content.get("number"),
                        "title": content.get("title"),
                        "url": f"https://github.com/{org_name}/issues/{content.get('number')}"
                    })
        
        print(f"\nFound {p0_count} open issue(s) with 'P0' label in project board")
        
        if p0_issues:
            print("\nP0 Issues:")
            for issue in p0_issues[:10]:  # Show first 10
                print(f"  - #{issue['number']}: {issue['title']} ({issue['url']})")
            if len(p0_issues) > 10:
                print(f"  ... and {len(p0_issues) - 10} more")
        
        return p0_count
        
    except Exception as e:
        print(f"Error accessing GitHub GraphQL API: {e}")
        raise


def main():
    """Main function to analyze P0 issues."""
    org_name = "tenstorrent"
    project_number = 248
    
    print(f"Analyzing GitHub project board:")
    print(f"  Organization: {org_name}")
    print(f"  Project: #{project_number}")
    print(f"  URL: https://github.com/orgs/{org_name}/projects/{project_number}/views/9")
    print()
    
    # Try GraphQL first (more accurate for project boards)
    try:
        print("Attempting to access project board via GraphQL API...")
        count = count_p0_issues_graphql(org_name, project_number)
        if count > 0:
            print(f"\n✓ Total P0 issues: {count}")
            return count
        else:
            # If GraphQL returns 0, it might be a scope issue, try REST API
            print("\nGraphQL returned 0 results. Trying REST API as fallback...")
            raise Exception("GraphQL returned 0 results")
    except Exception as e:
        if "Insufficient scopes" in str(e) or "INSUFFICIENT_SCOPES" in str(e):
            # Already printed message, continue to REST API
            pass
        else:
            print(f"\nGraphQL approach failed: {e}")
            print("Falling back to REST API search...")
        
        # Fallback to REST API
        try:
            count = count_p0_issues_rest_api(org_name, project_number)
            print(f"\n✓ Total P0 issues: {count}")
            return count
        except Exception as e2:
            print(f"\n❌ REST API approach also failed: {e2}")
            print("\nTroubleshooting tips:")
            print("1. Verify your GITHUB_TOKEN has 'repo' scope")
            print("2. Check that the organization name is correct")
            print("3. Ensure issues with 'P0' label exist and are open")
            sys.exit(1)


if __name__ == "__main__":
    main()

