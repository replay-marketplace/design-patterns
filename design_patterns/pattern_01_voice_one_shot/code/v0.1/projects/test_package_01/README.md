# Test Package 01

A simple Python program that demonstrates usage of `function_one` from `package_01`.

## Setup

### Option 1: Use the automated script (Recommended)

Simply run:
```bash
./runme.sh
```

This script will automatically:
- Create a virtual environment if needed
- Find the repository root and locate `package_01`
- Install `package_01` in editable mode
- Run the program

### Option 2: Manual setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   ```bash
   # On macOS/Linux:
   source venv/bin/activate
   
   # On Windows:
   venv\Scripts\activate
   ```

3. Install package_01 in editable mode:
   ```bash
   # The script automatically finds the correct path, but if installing manually:
   # Navigate to the repository root and find python_packages/package_01
   # Or use: pip install -e <path-to-repo-root>/python_packages/package_01
   ```

## Running the Program

```bash
python main.py
```

## Expected Output

```
Result 1: Hello world!
Result 2: Welcome to Python programming!
Result 3: test passed
Result 4: [INFO] prefix only
```

