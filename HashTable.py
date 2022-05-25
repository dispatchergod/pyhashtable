from enum import Enum


class HashTableNode(object):
    key = ""
    value = None
    next_node = None

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __getitem__(self, item):
        return self

    def get_node(self):
        return [self.key, self.value, self.next_node]


class Status(Enum):
    success = 0
    collision = 1
    error = -1


class HashTable(object):
    bucket = []

    def __init__(self, bucket_size):
        self.bucket = [None] * bucket_size

    def __getitem__(self, item):
        return self

    def find_index(self, hash_key):
        if hash_key is None:
            return Status.error

        return int(hash_key.encode("utf-8").hex(), 16) % len(self.bucket)

    def add_element(self, key, element):
        node = HashTableNode(key, element)
        index = self.find_index(key)
        aux_node = self.bucket[index]

        if aux_node is None:
            self.bucket[index] = node
            return Status.success

        while aux_node.next_node is not None:
            aux_node = aux_node.next_node

        aux_node.next_node = node
        return Status.collision

    def get_element(self, key):
        index = self.find_index(key)
        node = self.bucket[index]
        while node is not None:
            if node.key == key:
                return {key: node.value}
            else:
                node = node.next_node
        return "ERRoR: there is not element with this key"

