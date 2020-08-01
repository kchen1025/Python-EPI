from test_framework import generic_test
from test_framework.test_failure import TestFailure

from collections import OrderedDict

class Node:
    def __init__(self, key, price):
        self.key = key
        self.price = price
        self.next = None
        self.prev = None

class LruCache:
    def __init__(self, capacity: int) -> None:
        self.map = {}
        self.head = None
        self.tail = None
        self.capacity = 0
        self.maxCapacity = capacity

    def insert(self, isbn: int, price: int) -> None:
        if isbn in self.map:
            price = self.map[isbn].price
            self.erase(isbn)
        elif self.capacity == self.maxCapacity:
            keyToDelete = self.head.key
            self.erase(keyToDelete)

        newNode = self.addNode(isbn, price)
        self.map[isbn] = newNode
        self.capacity += 1

    def lookup(self, isbn: int) -> int:
        if isbn not in self.map: return -1

        price = self.map[isbn].price
        self.erase(isbn)
        self.insert(isbn, price)
        return price


    def erase(self, isbn: int) -> bool:
        if isbn not in self.map:
            return False

        nodeToDelete = self.map[isbn]
        self.deleteNode(nodeToDelete)
        del self.map[isbn]
        self.capacity -= 1
        return True

    # add node to end of LL, return new node
    def addNode(self, isbn, price):
        # create node
        newNode = Node(isbn, price)

        if self.tail:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        else:
            self.head = newNode
            self.tail = newNode
        return newNode

    def deleteNode(self, node):
        # find prev node
        prevNode = node.prev
        nextNode = node.next

        # delete
        if prevNode: prevNode.next = node.next
        if nextNode: nextNode.prev = prevNode

        # set new heads/tails
        if self.head == node:
            self.head = nextNode

        if self.tail == node:
            self.tail = prevNode




def lru_cache_tester(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure('Lookup: expected ' + str(cmd[2]) +
                                  ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure('Erase: expected ' + str(cmd[2]) + ', got ' +
                                  str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    # c = LruCache(3)
    # c.insert('abc',1)
    # c.insert('def',2)
    # c.insert('ghi',3)
    # c.insert('ghi',4)
    # c.insert('yeet',4)
    # c.erase('ghi')
    # c.erase('def')
    # c.erase('def')
    #
    # print(c.map, c.head.key, c.head.price, c.tail.key, c.tail.price)
    exit(
        generic_test.generic_test_main('lru_cache.py', 'lru_cache.tsv',
                                       lru_cache_tester))
