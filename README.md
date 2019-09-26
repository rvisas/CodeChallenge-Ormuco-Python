# CodeChallenge-Ormuco-Python
Package to provide a distributed LRU cache

### To Generate Source

* Move into the project folder
`$ cd $HOME/{root_folder}`

* Run the "dist" generator
`$ python setup.py sdist`

### To install the package

Follow the next steps

* Move into the project folder
`$ cd $HOME/{root_folder}`

* Run the pip installer
`$ pip install lru_cache-1.0.0.tar.gz`
 

### To publish the package in PyPI

Follow the next steps

* Move into the project folder
`$ cd $HOME/{root_folder}`

* Install twine
`$ python -m pip install --user --upgrade twine`

* Upload package to PyPI
`$ twine upload dist/lru_cache-1.0.0.tar.gz`

