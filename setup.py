
from setuptools import setup, find_packages

setup(
    name="grafanapy",
    version="0.1.0",
    description="Serve pandas DataFrames as Grafana-compatible JSON APIs",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "fastapi",
        "uvicorn",
        "pandas"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
