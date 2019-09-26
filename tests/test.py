import time
import unittest

from data import Data
from cache import LRUCache

# helper functions
def generate_data(n=5):
    users = []
    for i in range(1, n+1):
        username = 'user{}'.format(i)
        email = '{}@gmail.com'.format(username)
        user = Data(username, email)
        users.append(user)
    return users


class TestCache(unittest.TestCase):

    def test_expiry(self):
        cache = LRUCache(size=1000, expiry=2, region='US/EST')
        users = generate_data(n=5)
        for user in users:
            cache.put(user)

        # cache has 5 items?
        self.assertEqual(len(cache), 5)

        # sleep for 2 seconds, all items expired?
        time.sleep(2)
        cache.drop_expired()
        self.assertTrue(cache.is_empty())

        # remove expired items
        user1 = users[0]
        cache.put(user1)
        time.sleep(2)
        for user in users[1:]:
            cache.put(user)
        cache.drop_expired()
        self.assertEqual(len(cache), 4)

    def test_capacity(self):
        cache = LRUCache(size=3, expiry=1000, region='US/EST')
        users = generate_data(n=5)
        for user in users:
            cache.put(user)

        # lru should be user 3 and mru should be user 5
        self.assertEqual(cache.lru, users[2].key)
        self.assertEqual(cache.mru, users[-1].key)


if __name__ == '__main__':
    unittest.main()
