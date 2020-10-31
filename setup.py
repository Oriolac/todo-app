
from setuptools import setup, find_packages
from todo.core.version import get_version

VERSION = get_version()

f = open('README.md', 'r')
LONG_DESCRIPTION = f.read()
f.close()

setup(
    name='todo',
    version=VERSION,
    description='A simple TODO App',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    author='Oriol Alàs Cercós',
    author_email='oriolalascercos@gmail.com',
    url='https://github.com/johndoe/myapp/',
    license='Copyright (c) 2009-2019 Data Folk Labs, LLC',
    packages=find_packages(exclude=['ez_setup', 'tests*']),
    package_data={'todo': ['templates/*']},
    include_package_data=True,
    entry_points="""
        [console_scripts]
        todo = todo.main:main
    """,
)
