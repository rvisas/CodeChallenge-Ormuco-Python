# CodeChallenge-Ormuco-Python
Package to provide a distributed LRU cache.

At Ormuco, we want to optimize every bits of software we write. Your goal is to write a new library that can be integrated to the Ormuco stack. Dealing with network issues everyday, latency is our biggest problem. Thus, your challenge is to write a new Geo Distributed LRU (Least Recently Used) cache with time expiration. This library will be used extensively by many of our services so it needs to meet the following criteria:
 
* Simplicity. Integration needs to be dead simple.
* Resilient to network failures or crashes.
* Near real time replication of data across Geolocation. Writes need to be in real time.
* Data consistency across regions
* Locality of reference, data should almost always be available from the closest region
* Flexible Schema
* Cache can expire

As a hint, we are not looking for quantity, but rather quality, maintainability, scalability, testability and a code that you can be proud of. When submitting your code add the necessary documentation to explain your overall design and missing functionalities.  Do it to the best of your knowledge.
 

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


### To test the solution

Follow the next steps

* Move into the project folder
`$ cd $HOME/{root_folder}`

* Execute test file
`$ python3 ./ronny_visa_test.py`
