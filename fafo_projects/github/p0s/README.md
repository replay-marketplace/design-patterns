# GitHub P0 Issues Analyzer

This script analyzes a GitHub project board and counts how many open issues have the "P0" label.

## Quick Start

The easiest way to run the analyzer is using the setup script:

```bash
./setup.sh
```

This will:
- Create and activate a Python virtual environment
- Install all dependencies
- Run the analyzer

**Note:** Make sure to set your GitHub token first:
```bash
export GITHUB_TOKEN=your_github_token_here
```

## Manual Setup

If you prefer to set up manually:

1. Create and activate virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up GitHub token:
```bash
export GITHUB_TOKEN=your_github_token_here
```

To create a GitHub token:
1. Go to https://github.com/settings/tokens
2. Click "Generate new token" → "Generate new token (classic)"
3. Give it a name (e.g., "P0 Issues Analyzer")
4. Select scopes:
   - `repo` (Full control of private repositories)
   - `read:org` (Read org and team membership)
   - `read:project` (Read project boards - required for GraphQL API)
5. Click "Generate token"
6. Copy the token and set it as an environment variable

## Usage

After setup, you can run:
```bash
python analyze_p0_issues.py
```

Or use the setup script which does everything:
```bash
./setup.sh
```

The script will:
1. Connect to the GitHub project board at: https://github.com/orgs/tenstorrent/projects/248
2. Analyze open issues
3. Count issues with the "P0" label
4. Display the count and list of P0 issues

## How it works

The script uses two approaches:
1. **GraphQL API** (primary): Directly queries the project board to get issues
   - Requires `read:project` scope
   - More accurate for project boards
2. **REST API** (fallback): Searches all repositories in the organization for open issues with P0 label
   - Only requires `repo` scope
   - Searches across all repositories in the organization

**Note:** If you see "0 P0 issues" but know there are some, it's likely because:
- GraphQL failed due to missing `read:project` scope and REST API search didn't find them
- The label might be named differently (case sensitivity, spacing, etc.)
- Issues might be in private repos that your token can't access

The script will automatically fall back to REST API if GraphQL fails due to scope issues.

