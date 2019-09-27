import time
import unittest

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

    def test_expiry(self):
        cache = LRUCache(20, 1200)
        users = generate_data(20)
        for (username, email) in users:
            cache.put(username, email)

        # cache has 5 items?
        self.assertEqual(cache.getLength(), 20)

        # sleep for 5 seconds, all items expired?
        time.sleep(5)
        cache.removeExpiredNodes()
        self.assertTrue(cache.getLength() == 0)

    def test_capacity(self):
        cache = LRUCache(3, 1000)
        users = generate_data(20)
        for user in users:
            cache.put(user)

        # lru should be user 3 and mru should be user 5
        self.assertEqual(cache.lru, users[2].key)
        self.assertEqual(cache.mru, users[-1].key)

if __name__ == '__main__':
    unittest.main()
