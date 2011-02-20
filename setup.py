from setuptools import setup, find_packages

setup(
    name='simpleblog', 
    version='0.1',
    author='Ben Davis',
    author_email='ben@savidworks.com',
    url='http://www.savidworks.com',
    description='A simple django blog',
    keywords='blog',
    packages = find_packages(),
    include_package_data = True
)
