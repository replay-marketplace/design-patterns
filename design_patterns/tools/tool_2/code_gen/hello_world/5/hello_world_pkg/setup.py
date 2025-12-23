from setuptools import setup, find_packages

setup(
    name="hello_world",
    version="0.1.0",
    description="A simple hello world package",
    author="Your Name",
    author_email="your.email@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        # Add your dependencies here
    ],
)

