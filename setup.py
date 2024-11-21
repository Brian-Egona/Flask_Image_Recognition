from setuptools import setup, find_packages

setup(
    name='Flask Image Recognition',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Flask',
        'werkzeug==1.0.1',
        'pytest',  # Any other dependencies
    ],
)
