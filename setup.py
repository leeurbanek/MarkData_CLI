"""To install use: pip install -e . or python setup.py develop"""
from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        return content.split('\n')


with open('README.md', 'r') as fh:
    long_description = fh.read()


setup(
    name="markdata-cli",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    description="MarkData_CLI: stock MARKet DATA Command Line Interface",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    install_requires=get_requirements(),
    entry_points={
        'console_scripts': [
            'markdata-cli=src.run:main_cli',
        ]
    }
)
