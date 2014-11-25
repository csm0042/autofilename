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

    scripts=['scripts/main.py'],
    #console=['scripts/main.py'],
    windows=['scripts/main.py'],

    options={'py2exe': {'bundle_files': 2, 'compressed': True}},
    zip_safe=False,
    )

#packages=find_packages('src'),      # Include all packages under 'src' folder
    #console=[{'src': '_main.py'}],
    #options={'py2exe': {
    #    'packages': 'encodings, src',
    #         'includes': None},
    #         },


    #package_dir={'':'src'},             # Tell setuptools that packages are under 'src' folder
    #include_package_data=True,          # Include everything found in source control folder
    #exclude_package_data={'':['README.TEXT']},