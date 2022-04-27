from setuptools import find_packages
from setuptools import setup


with open("README.md") as f:
    LONG_DESCRIPTION = f.read()


setup(
    name="sky130",
    version="0.0.4",
    url="https://github.com/gdsfactory/skywater130",
    include_package_data=True,
    license="MIT",
    author="gdsfactory",
    description="skywater gdsfactory pdk",
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests",)),
    install_requires=("gdsfactory",),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
    ],
)
