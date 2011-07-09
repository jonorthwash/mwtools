try: 
	import distribute_setup
	distribute_setup.use_setuptools()
except: pass

from setuptools import setup, find_packages
from os import listdir

setup(
	name = "mwparser",
	version = "0.7",
	packages = ["mwparser"],
	#scripts = scripts,

	author = "Brendan Molloy",
	author_email = "brendan@bbqsrc.net",
	description = """Parses Mediawiki syntax into readable plain-text suitable
	for linguistic purposes.
	""",
	license = "CC0",
	keywords = "mediawiki wikipedia parser"
)
