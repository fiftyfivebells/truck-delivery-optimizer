import random as r

# the number of bytes in an integer
w = 32


class HashTable(object):
    def __init__(self):
        self.__initialize()

    def __initialize(self):
        self.size = 0
        self.dimension = 1
        self.seed = self.__random_odd_int()
        self.array = self.__allocate_backing_array(2 ** d)

    def add(self, val):
        pass

    def remove(self, val):
        pass

    def find(self, val):
        pass

    def clear(self):
        pass

    def __resize(self):
        pass

    def __hash(self, val):
        pass

    def __allocate_backing_array(self, size):
        pass

    def __random_odd_int(self):
        pass

    def __iter__(self):
        pass
