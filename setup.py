from setuptools import setup, find_packages
import os

required = list()

with open(os.path.join("resources", "requirements.txt")) as f:
    required = f.read().splitlines()

setup(
    name="content_scraper",
    version="0.1.0",
    url="https://sindrisforge.com/opskit",
    author="Jagath Jai Kumar",
    description="Scraper for pulling content from various sources",
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms="any",
    install_requires=required,
)
