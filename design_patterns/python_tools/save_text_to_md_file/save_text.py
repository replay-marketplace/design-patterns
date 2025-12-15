#!/usr/bin/env python3
"""
Simple program that receives a string and saves it to a markdown file.
"""

import sys
import argparse
from datetime import datetime
from pathlib import Path


def generate_timestamp_filename() -> str:
    """
    Generate a filename with timestamp in format YYYYMMDD-HHMMSS.md
    
    Returns:
        Filename string in format YYYYMMDD-HHMMSS.md
    """
    now = datetime.now()
    return now.strftime("%Y%m%d-%H%M%S.md")


def save_text_to_file(text: str, filename: str) -> None:
    """
    Save a string to a file in the output/ directory.
    
    Args:
        text: The string content to save
        filename: The name of the file to save to
    """
    try:
        # Create output directory if it doesn't exist
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Save the file to output directory
        file_path = output_dir / filename
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"✅ Text saved successfully to {file_path}")
    except Exception as e:
        print(f"❌ Error saving file: {e}", file=sys.stderr)
        sys.exit(1)


def main():
    """Main function to handle command-line arguments or interactive input."""
    parser = argparse.ArgumentParser(
        description="Save a string to a markdown file"
    )
    parser.add_argument(
        'text',
        nargs='?',
        help='The text string to save (optional, will prompt if not provided)'
    )
    parser.add_argument(
        '-f', '--filename',
        default=None,
        help='Output filename (default: auto-generated timestamp YYYYMMDD-HHMMSS.md)'
    )
    
    args = parser.parse_args()
    
    # If text is provided as argument, use it; otherwise prompt user
    if args.text:
        text = args.text
    else:
        print("Enter the text to save (press Ctrl+D or Ctrl+Z when done):")
        try:
            text = sys.stdin.read()
        except KeyboardInterrupt:
            print("\n❌ Cancelled by user", file=sys.stderr)
            sys.exit(1)
    
    if not text.strip():
        print("❌ No text provided", file=sys.stderr)
        sys.exit(1)
    
    # Use provided filename or generate timestamp-based filename
    filename = args.filename if args.filename else generate_timestamp_filename()
    save_text_to_file(text, filename)


if __name__ == "__main__":
    main()

