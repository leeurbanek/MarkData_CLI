"""from this directory use: pip install -e . or python setup.py develop"""
from setuptools import setup, find_packages


def get_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        return content.split('\n')


setup(
    name="markdata",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=get_requirements(),
    entry_points="""
        [console_scripts]
        MarkData_CLI=app.cli:run
    """,
)
