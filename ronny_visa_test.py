import unittest

from src.lru_cache.node import Node
from src.lru_cache.cache import LRUCache


class TestCache(unittest.TestCase):

    def test_max_capacity(self):
        cache = LRUCache(5, 1000)
        cache.put('key1', 'value1')
        cache.put('key2', 'value2')
        cache.put('key3', 'value3')
        cache.put('key4', 'value4')
        cache.put('key5', 'value5')
        cache.put('key6', 'value6')

        self.assertEqual(cache.getLength(), 5)

    def test_lru_policy(self):
        cache = LRUCache(5, 1000)
        #print(cache)
        cache.put('key1', 'value1')
        #print(cache)
        cache.put('key2', 'value2')
        #print(cache)
        cache.get('key1')
        #print(cache)
        cache.put('key3', 'value3')
        #print(cache)

        self.assertEqual(cache.getLength(), 3)
        self.assertEqual(cache.getHead(), 'key3')
        self.assertEqual(cache.getTail(), 'key2')


if __name__ == '__main__':
    unittest.main()
