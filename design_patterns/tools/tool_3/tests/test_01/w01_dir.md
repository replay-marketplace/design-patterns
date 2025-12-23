Example dir structure:
```
├── module_00/
│   ├── setup_and_run.sh            ← sets up python venv, installs requirements, runs the tests.  
│   ├── requirements.txt
│   ├── src/
│   │   ├── __init__.py
│   │   ├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
│   │   ├── <function_1>.py         # Empty
│   │   ├── <function_2>.py         # Empty
│   ├── tests/
│   │   └── test.py
│   ├── replay/
│   │   ├── .reports.md
│   │   ├── prompt.md
├── module_01/
│   ├── setup_and_run.sh            ← sets up python venv, installs requirements, runs the tests.  
│   ├── requirements.txt
│   ├── src/
│   │   ├── __init__.py
│   │   ├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
│   │   ├── <function_1>.py         # Empty
│   │   ├── <function_2>.py         # Empty
│   ├── tests/
│   │   └── test.py
│   ├── replay/
│   │   ├── .reports.md
│   │   ├── prompt.md
├── .reports.md
```