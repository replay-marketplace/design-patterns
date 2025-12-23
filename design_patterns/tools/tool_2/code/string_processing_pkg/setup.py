"""
Setup configuration for string_processing_pkg.
"""

from setuptools import setup, find_packages

with open("README_API_SIGNATURE.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="string-processing-pkg",
    version="0.1.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="A Python package with string processing utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/string_processing_pkg",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    python_requires=">=3.8",
    install_requires=[],
)


