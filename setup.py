from setuptools import setup, find_packages

def readme():
    with open('README.md') as f:
        return f.read()
setup(
    name="garfieldcsv",
    version="0.4.2",
    author="Liu Wenyuan",
    description="A set of Python scripts that converts comic transcripts from john.ccac.rwth-aachen.de (like Garfield.txt) into CSV files",
    long_description=readme(),

    url="https://github.com/Dobby233Liu/garfield.csv", 

    packages=['garfieldcsv', 'garfieldcsv.sanitizer', 'garfieldcsv.enc_converter'],
    zip_safe=False,
    python_requires=">=3.8",
)