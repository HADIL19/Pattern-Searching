from setuptools import setup, find_packages
version='0.1.3' # or 0.2.0 if major changes
setup(
    name="pattern_searching",  # package name, must be unique on PyPI
    version=version,
    author="Hadil Khelif",
    author_email="hadylkhelif18@gmail.com",
    description="Single-pattern and multiple-pattern string searching algorithms in Python",
    long_description=open("README.md", "r", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/HADIL19/Pattern-Searching",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
