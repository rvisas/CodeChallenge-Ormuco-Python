from .node import Node

class LRUCache:

    def __init__(self, max_capacity=10, expiry=3600):
        self._max_capacity = max_capacity
        self._expiry = expiry
        self._cache = dict()
        self._head = None
        self._tail = None

    def get(self, key):
        if (key in self._cache):
            node = self._cache[key]
            self.deleteFromList(node)
            self.insertHead(node)
            return node.getValue()
        else:
            return None

    def deleteFromList(self, node):
        prevNode = node.getPrev()
        nextNode = node.getNext()
        if ((prevNode == None) and (nextNode == None)):
            self._head = None
            self._tail = None
        elif (prevNode == None):
            self._head = nextNode
            self._cache[self._head].setPrev(None)
        elif (nextNode == None):
            self._tail = prevNode
            self._cache[self._tail].setNext(None)
        else:
            self._cache[prevNode].setNext(nextNode)
            self._cache[nextNode].setPrev(prevNode)

        del self._cache[node.getKey()]

    def insertHead(self, node):
        self._cache[node.getKey()] = node
        node.setNext(self._head)
        self._head = node.getKey()

    def put(self, key, value):
        node = None
        if (key in self._cache):
            node = self._cache[key]
            node.setValue(value)
            self.deleteFromList(node)
        else:
            if (len(self._cache) >= self._max_capacity):
                self.deleteFromList(self._cache[self._tail])
            node = Node(key, value)

        self.insertHead(node)

    def removeExpiredNodes(self):
        for node in self._cache.values():
            if (node.isExpired(self._expiry)):
                self.deleteFromList(node)

    def getLength(self):
        return len(self._cache)
