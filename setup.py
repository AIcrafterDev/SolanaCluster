
from setuptools import setup, find_packages

setup(
    name="cluster",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "solana",
        "solders",
    ],
    extras_require={
        "dev": ["pytest", "flake8", "pre-commit"],
        "prod": ["gunicorn"],
    },
    entry_points={
        "console_scripts": [
            "cluster=cluster.main:main",
        ],
    },
)
