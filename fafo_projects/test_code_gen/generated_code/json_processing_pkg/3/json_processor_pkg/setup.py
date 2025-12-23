from setuptools import setup, find_packages

setup(
    name="json_processor",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "jsonschema>=4.0.0",
    ],
    author="JSON Processor Team",
    description="A comprehensive JSON file processing package",
    python_requires=">=3.6",
)
