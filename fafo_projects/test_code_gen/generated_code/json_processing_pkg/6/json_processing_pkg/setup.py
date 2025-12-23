from setuptools import setup, find_packages

setup(
    name="json_processing",
    version="0.1.0",
    description="JSON processing utilities for file operations",
    author="Code Generator",
    author_email="code@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "jsonschema>=4.0.0",
    ],
)
