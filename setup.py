from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in hire_store/__init__.py
from hire_store import __version__ as version

setup(
	name="hire_store",
	version=version,
	description="Hire Store Management System",
	author="efeone private limited",
	author_email="jamsheerak678@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
