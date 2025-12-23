from setuptools import setup, find_packages

setup(
    name="agent_chat",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "anthropic>=0.18.0",
        "python-dotenv>=1.0.0",
    ],
    author="Your Name",
    description="A Python package for Anthropic AI chat agent functions",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
