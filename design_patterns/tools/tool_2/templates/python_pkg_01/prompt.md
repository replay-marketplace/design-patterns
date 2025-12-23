Generate this project template in the folder /template.


Example dir structure
```
<package_name>_pkg/
├── setup.py              ← At root (standard Python practice)
├── README_API_SIGNATURE.md     ← Absolute minimilistic file with listed apis (`dir_exists(filepath: str) -> bool` - Check existence)
├── <package_name>/          ← Package directory
│   ├── __init__.py
│   ├── <function_1>.py         # Empty
│   ├── <function_2>.py         # Empty
└── tests/
    ├── test.py
    ├── setup_and_run.sh
    ├── requirements.txt
    └── venv/
```
