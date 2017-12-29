"""Installation script for {{ .Name }}."""

from setuptools import setup

try:
    with open("README.md", "r") as f:
        README = f.read()
except:
    README = __doc__

try:
    fp = open("requirements.txt", "r")
    requirements = fp.readlines()
    fp.close()
except:
    requirements = []


setup(
    name='{{ .Name }}',
    version='0.1.0',
    author='{{ .Author }}',
    author_email='{{ .AuthorEmail }}',
    long_description=README,
    include_package_data=True,
    zip_safe=False,
    install_requires=requirements
)
