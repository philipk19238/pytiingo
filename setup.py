from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="pytiingo",
    version="0.0.1",
    description="Python SDK for Tiingo Financial Markets API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Philip Kung",
    author_email="pkung67@utexas.edu",
    url="https://github.com/philipk19238/pytiingo",
    packages=find_packages(),
    install_requires=[
        'requests',
        'python-dotenv',
        'pandas',
        'pydantic'
    ]
)
