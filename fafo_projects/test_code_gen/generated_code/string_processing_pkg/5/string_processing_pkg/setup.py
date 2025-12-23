from setuptools import setup, find_packages

setup(
    name="string_processing",
    version="0.1.0",
    description="A package for string processing and analysis functions",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        # No external dependencies required for basic functionality
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
        ],
    },
)
