from setuptools import setup, find_packages

setup(
    name='indoor_outdoor_pytorch',
    author='',
    version='0.1',
    packages=find_packages(exclude=['tests']),
    license='Private',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    zip_ok=False,
)
