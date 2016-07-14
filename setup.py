from setuptools import setup, find_packages
import py2exe


def readme():
    with open('README.rst') as f:
        return f.read()


setup(
    name='autofilename',
    version='1.2.0',
    description='Auto File-Rename Utility',
    long_description=readme(),

    author='Christopher Maue',
    author_email='csmaue@gmail.com',
    license='GNUv2',
    url='https://github.com/csm0042/src.git',

    packages=['autofilename'],
    include_package_data=True,

    scripts=['autofilename/main.py'],
    #console=['autofilename/main.py'],
    windows=['autofilename/main.py'],

    options={'py2exe': {'bundle_files': 2, 'compressed': True}},
    zip_safe=False,
    )