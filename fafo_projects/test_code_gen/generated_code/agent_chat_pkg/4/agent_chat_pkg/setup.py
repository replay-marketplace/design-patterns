from setuptools import setup, find_packages

with open("README_API_SIGNATURE.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="agent_chat",
    version="0.1.0",
    description="Agent chat functions using DeepSeek API for code generation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Agent Chat Developer",
    author_email="developer@example.com",
    packages=find_packages(),
    python_requires=">=3.7",
    install_requires=[
        "requests>=2.28.0",
        "python-dotenv>=1.0.0",
    ],
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
