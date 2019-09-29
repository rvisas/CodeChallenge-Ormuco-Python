import time
import unittest

print("Value: {}".format(__name__))

from src.lru_cache.node import Node
from src.lru_cache.cache import LRUCache

def generate_data(n=10):
    users = []
    for number in range(n):
        username = 'ronny{}'.format(number)
        email = '{}@ormuco.com'.format(username)
        users.append((username, email))
    return users

class TestCache(unittest.TestCase):

    # def test_expiry(self):
    #     cache = LRUCache(20, 1200)
    #     users = generate_data(20)
    #     for (username, email) in users:
    #         cache.put(username, email)

    #     self.assertEqual(cache.getLength(), 20)

    #     # sleep for 5 seconds, all items expired?
    #     time.sleep(5)
    #     cache.removeExpiredNodes()
    #     self.assertTrue(cache.getLength() == 0)

    def test_capacity(self):
        cache = LRUCache(5, 1000)
        cache.put('key1', 'value1')
        cache.put('key2', 'value2')
        cache.put('key3', 'value3')
        cache.put('key4', 'value4')
        cache.put('key5', 'value5')
        cache.put('key6', 'value6')

        # lru should be user 3 and mru should be user 5
        self.assertEqual(cache.getLength(), 5)   

if __name__ == '__main__':
    unittest.main()
