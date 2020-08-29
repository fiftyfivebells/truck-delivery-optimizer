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

    # Resizes the backing array of the hash table in O(n) time. First it determins the new dimension of the
    # hash table by finding the power of 2 that is less than or equal to the number of items in the table.
    # Then it creates a new array with that power of 2 empty spots. It then re-hashes all of the values in the
    # original backing array and puts them into the new array.
    def __resize(self):
        self.dimension = 1
        while (2 ** self.dimension) <= self.size:
            self.dimension += 1

        self.size = 0
        old_array = self.array
        self.array = self.__allocate_backing_array(2 ** self.dimension)

        for i in range(len(old_array)):
            for x in old_array[i]:
                self.add(x)

    def __hash(self, val):
        hashed_val = ((self.seed * int(val)) % 2 ** w) // 2 ** (w - self.dimension)
        return ((self.seed * hashed_val) % 2 ** w) // 2 ** (w - self.dimension)

    def __allocate_backing_array(self, size):
        return [[] for _ in range(size)]

    def __random_odd_int(self):
        return r.randrange(2 ** w) | 1  # gets random int in range 1 - 2^32, then ORs it with 1 to make it odd

    def __iter__(self):
        pass
