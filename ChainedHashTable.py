# Stephen Bell: #001433854

import random as r

# the number of bytes in an integer
w = 32


class HashTable(object):
    def __init__(self):
        self.__initialize()

    # Initializes the internal structure. Sets the size of the hash table to 0, sets the dimension to
    # 1, gets the random number for hashing, and creates a backing array to store elements.
    def __initialize(self):
        self.size = 0  # number of items in the table
        self.dimension = 1  # dimension used by the hashing function
        self.seed = self.__random_odd_int()  # seed used by the hashing function
        self.array = self.__allocate_backing_array(2 ** self.dimension)  # backing array to hold lists of items

    # Inserts a new key/value pair into the table in O(1) amortized time. Each call to resize is O(n), but
    # resize should only be called occasionally.
    def insert(self, key, val):
        if self.size + 1 > len(self.array):
            self.__resize()

        # if the key already exists, get rid of it before inserting a new one
        if self.find(key) is not None:
            self.array[self.__hash(key)].remove((key, val))

        self.array[self.__hash(key)].append((key, val))
        self.size += 1

    # Updates the value associated with the given key to the new value. Operates in O(1) time, since the
    # size of the array at each index in the backing array is very small (since the hashing function is good)
    def update(self, key, val):
        self.find(key)
        hashed = self.__hash(key)
        for i in range(len(self.array[hashed])):
            if self.array[hashed][i][0] == key:
                self.array[hashed][i] = (key, val)


    # Removes the item with the specified key in amortized O(1) time. Each call to resize is O(n), but 
    # reize should only be called occasionally, allowing the cost to be amortized. Returns None if the
    # key is not in the list.
    def remove(self, key):
        elements = self.array[self.__hash(key)]
        for x in elements:
            if x[0] == key:
                elements.remove(x)
                self.size -= 1
                if 3 * self.size < len(self.array):
                    self.__resize()
                return x
        return None

    # Finds and returns the value associated with the given key, or None if the key doesn't exist. This
    # is O(1) in practice, because even though we iterate the list at each index, the number of items in
    # the list is very small.
    def find(self, key):
        for x in self.array[self.__hash(key)]:
            if x[0] == key:
                return x[1]
        return None

    # Allows use of bracket notation to get value associated with a certain key. Will raise an error
    # if the key does not exist
    def __getitem__(self, key):
        return self.find(key)

    # Allows use of bracket notation to set a new value for the given key. Raises a KeyError if the key
    # does not exist in the backing array
    def __setitem__(self, key, val):
        self.insert(key, val)

    # O(n) time. Sets the dimension back to 1, creates a new backing array of size 2, and then sets the
    # number of items currently in the list back to 0
    def clear(self):
        self.dimension = 1
        self.array = self.__allocate_backing_array(2)
        self.size = 0

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
                self.insert(x[0], x[1])

    # Generates a hash value in O(1) time. First it creates a hash from the given value by multiplying it by a
    # random 32 bit number, the getting the remainder of that divided by 2**32 (to throw away some of the bits),
    # then dividing by another large number to throw away more bits, creating a value that is within the size
    # of the backing array. The function is done again using the hashed value in place of the original value
    # to reduce collisions.
    def __hash(self, val):
        return ((self.seed * hash(val)) % 2 ** w) // 2 ** (w - self.dimension)

    # Creates a new backing array in O(n) time. This simply takes in a size value, then creates a list of
    # size "size" with an empty list at each index. This is linear time because it goes from index 0 to
    # size - 1 putting empty lists at each point.
    def __allocate_backing_array(self, size):
        return [[] for _ in range(size)]

    # Generates a random odd integer in O(1) time. This is constant because the randrange function creates
    # a random integer in constant time, and then a bitwise OR operation is done with 1 to ensure that the
    # last bit is a 1, ie. that the number is random.
    def __random_odd_int(self):
        return r.randrange(2 ** w) | 1  # gets random int in range 1 - 2^32, then ORs it with 1 to make it odd

    # Allows users to iterate over the hash table with for loops. This is an O(n) time operation because it
    # touches every item in the list once in order to iterate everything it contains
    def __iter__(self):
        for elements in self.array:
            for x in elements:
                yield x[0], x[1]

    # Checks whether the provided key is in the hash table. This is an O(1) operation, because even though it
    # is iterating the list contained at a certain index in the backing array, that list is guaranteed to be
    # small, so it is effectively constant time.
    def __contains__(self, key):
        for element in self.array[self.__hash(key)]:
            if element[0] == key:
                return True
        return False
