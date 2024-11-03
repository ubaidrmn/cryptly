from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name="cryptly",
    version="0.1.0",
    packages=find_packages(),
    author="Ubaid Ur Rehman",
    author_email="rehmanubaid2003@gmail.com",
    description="A Python library implementing common encryption and cipher techniques, providing easy-to-use functions for encryption and decryption.",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.0",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
)
