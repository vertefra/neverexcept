# type: ignore
import setuptools

with open('README.md',"r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="neverexcept",
    version="0.0.1",
    author="Vertemati Francesco",
    description="Use result patter to create function that never throw exceptions",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.10"
    ],
    python_requires = '>=3.10',
    py_modules="neverexcept",
    package_dir={"":"."},
    install_requires=[]
)