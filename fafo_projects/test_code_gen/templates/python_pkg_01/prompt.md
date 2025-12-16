Generate this project template in the folder /template

Example dir structure
```
├── <package_name>/                 # Python package
│   ├── __init__.py
│   ├── <function_1>.py         # Empty
│   ├── <function_2>.py         # Empty
│   ├── setup.py
│   └── README.md                   # Extreamly simple (install, function signatures)
├── tests/
│   └── venv/
│   └── test.py
│   └── requirements.txt
│   └── setup_and_run.sh        # Extreamly simple script to tarts the python env, install dependencies, and run the tests


<package_name>_pkg/
├── setup.py              ← At root (standard Python practice)
├── README.md
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
