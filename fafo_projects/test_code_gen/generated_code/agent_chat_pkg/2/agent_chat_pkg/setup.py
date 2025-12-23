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
    description="A package for interacting with Anthropic's Claude AI for chat and code generation",
    python_requires=">=3.7",
)
