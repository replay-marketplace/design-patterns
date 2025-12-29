
Implement  2 modules, each with the structure below: module1, module2. 

## Module1:
`add(a: int, b: int) -> int'
`sub(a: int, b: int) -> int'

## Module2:
`calculate(a: int, b: int, type: str) -> int'  # Make sure to use add() and sub() from module!!!


Example dir structure
```
dir_structure/
├── module1/                        # module1     
│   ├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
│   ├── module1/
│   │   ├── __init__.py
│   │   ├── add.py
│   │   ├── sub.py
│   └── tests/
│       ├── test.py                 # Clean imports: `from module1 import add, sub` (no sys.path manipulation)
│       ├── run_tests.sh            # Test runner that sets PYTHONPATH and runs tests
│       ├── setup.sh                # Make python env, install requirements, set PYTHONPATH in venv activation
│       ├── requirements.txt
│       ├── README.md               # Absolute minimum possible readme, just one line how to run the test

│       └── venv/
└── module2/                        # module2     
    ├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
    ├── module2/
    │   ├── __init__.py
    │   ├── calculator.py
    └── tests/
        ├── test.py                 # Clean imports: `from module2 import calculate` (no sys.path manipulation)
        ├── run_tests.sh            # Test runner that sets PYTHONPATH and runs tests
        ├── setup.sh                # Make python env, install requirements, set PYTHONPATH in venv activation
        ├── README.md               # Absolute minimum possible readme, just one line how to run the test
        ├── requirements.txt
        └── venv/
```

## Import Strategy (Avoid sys.path.insert and pip install -e)

**PYTHONPATH in setup.sh **
- In `setup.sh`: After creating venv, add `export PYTHONPATH="${PYTHONPATH}:$(cd .. && pwd)"` to venv/bin/activate
- Or set it in a test runner script `run_tests.sh`: `PYTHONPATH="$(dirname "$0")/.." python test.py`
- Test files use clean imports: `from module1 import add, sub`
