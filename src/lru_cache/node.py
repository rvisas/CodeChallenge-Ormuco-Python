import time


class Node:

    def __init__(self, key=None, value=None, prev=None, next=None):
        self._key = key
        self._value = value
        self._prev = prev
        self._next = next
        self._creation_time = time.time()

    def getKey(self):
        return self._key

    def setKey(self, key=None):
        self._key = key

    def getValue(self):
        return self._value

    def setValue(self, value=None):
        self._value = value

    def getPrev(self):
        return self._prev

    def setPrev(self, prev=None):
        self._prev = prev

    def getNext(self):
        return self._next

    def setNext(self, next=None):
        self._next = next

    def isExpired(self, expiry):
        elapsedTime = time.time() - self._creation_time
        if (elapsedTime > expiry):
            return True
        else:
            return False

    def __repr__(self):
        return 'Node:{}, key:{}, value:{}, prev:{}, next:{}\n'.format(self._creation_time, self._key, self._value, self._prev, self._next)
