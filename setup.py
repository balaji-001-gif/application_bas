from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

from application_bas import __version__ as version

setup(
	name="application_bas",
	version=version,
	description="Application Bas",
	author="Balaji K",
	author_email="balajik@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
