try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup

config = {
	'description': 'Command line version of Klondike Solitaire written in Python',
	'author': 'Justin Drennen',
	'url': '',
	'download_url': '',
	'author_email': 'justin@drennentech.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['NAME'],
	'scripts': [],
	'name': 'PyKlondike'
}

setup(**config)
