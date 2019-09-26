from setuptools import setup, find_packages

setup(
    name='lru_cache',
    version='1.0.0',
    author='Ronny Visa',
    description='Package for implementing LRU cache',
    packages=find_packages('src'),
    package_dir={'': 'src'}
)
