'''
module defines the meta information for project and its required dependencies.
'''
from setuptools import setup, find_packages


setup(
    name='analytics-pf',
    version='0.0.1',
    description='analytics core platform',
    long_description='analytics core platform',
    author='NEC Labs',
    author_email='agoyal@nec-labs.com',
    packages=find_packages(),
    install_requires=['luigi', 'pyhs2', 'psutil', 'prettytable', 'pyyaml', 'psycopg2'],
    tests_require=['nosexcover'],
)
