try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Automatic File-name assigner',
	'author': 'Chris Maue',
	'author_email': 'csmaue@gmail.com',
    'url': 'https://github.com/csm0042/autofilename.git',
    'download_url': 'https://github.com/csm0042/autofilename.git',
	'version': '1.0.0',
	'packages': ['autofilename'],
	'name': 'auto-file-name'
}
setup(**config)