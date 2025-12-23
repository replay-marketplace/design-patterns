#!/usr/bin/env python3
"""
Setup script for test_tool_2 project.
Creates virtual environment and installs requirements.
"""

import os
import sys
import subprocess
from pathlib import Path

def main():
    """Create virtual environment and install requirements."""
    script_dir = Path(__file__).parent.resolve()
    venv_dir = script_dir / "venv"
    
    print("Setting up virtual environment for test_tool_2...")
    print("=" * 50)
    
    # Create virtual environment if it doesn't exist
    if not venv_dir.exists():
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", str(venv_dir)], check=True)
        print("✓ Virtual environment created")
    else:
        print("✓ Virtual environment already exists")
    
    # Determine the correct pip path based on OS
    if sys.platform == "win32":
        pip_path = venv_dir / "Scripts" / "pip"
        python_path = venv_dir / "Scripts" / "python"
    else:
        pip_path = venv_dir / "bin" / "pip"
        python_path = venv_dir / "bin" / "python"
    
    # Upgrade pip
    print("Upgrading pip...")
    subprocess.run([str(python_path), "-m", "pip", "install", "--upgrade", "pip"], check=True)
    print("✓ Pip upgraded")
    
    # Install requirements
    requirements_file = script_dir / "requirements.txt"
    if requirements_file.exists():
        print("Installing requirements from requirements.txt...")
        subprocess.run([str(pip_path), "install", "-r", str(requirements_file)], check=True)
        print("✓ Requirements installed")
    else:
        print("⚠ Warning: requirements.txt not found, skipping installation")
    
    print()
    print("=" * 50)
    print("✓ Setup complete!")
    print()
    print("To activate the virtual environment, run:")
    if sys.platform == "win32":
        print(f"  {venv_dir / 'Scripts' / 'activate'}")
    else:
        print(f"  source {venv_dir / 'bin' / 'activate'}")
    print()
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

