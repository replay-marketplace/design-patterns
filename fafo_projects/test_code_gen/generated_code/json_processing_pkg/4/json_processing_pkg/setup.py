from setuptools import setup, find_packages

with open("README_API_SIGNATURE.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="json_processing",
    version="0.1.0",
    description="A comprehensive JSON processing package with file I/O, validation, and directory operations",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="JSON Processing Team",
    author_email="json.processing@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "jsonschema>=4.0.0",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
