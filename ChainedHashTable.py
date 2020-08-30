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

    # Adds a new value to the hash table in amortized O(1) time. Most add operations are constant, because
    # all that happens is the internal size counter is incremented and the value is stored at the index
    # corresponding to its hashed value. However, when the number of elements in the table is equal to the
    # size of the backing array, the method has to call resize(), which is O(n). This is guaranteed to only
    # happen infrequently, so the cost of resizing is spread out over all the other adds that didn't need
    # a resize, making this an amortized O(1) method.
    def add(self, val):
        if self.size + 1 > len(self.array):
            self.__resize()

        self.array[self.__hash(val)].append(val)
        self.size += 1

    # Removes the given value in amortized O(1) time. Most remove operations are constant because they
    # don't need to resize the internal array. However, when the number of empty spaces in the array
    # becomes too large (if the filled spaces are less than 1/3 of the size of the backing array), the
    # backing array is resized to save space. This is an O(n) operation, but because it only happens
    # occasionally, it is amortized and the complexity is O(1).
    def remove(self, val):
        elements = self.array[self.__hash(val)]
        for x in elements:
            if x == val:
                elements.remove(val)
                self.size -= 1
                if 3 * self.size < len(self.array):
                    self.__resize()
                return x
        return None

    # Finds the given value in O(1) time. Technically it could be called O(n), because it iterates the
    # list of values stored at the index of the backing array corresponding to the hash of the given
    # value. However, the length of the list at each index should be very small assuming a good hashing
    # function, so because we're only iterating a couple values, it is effectively O(1) in practice.
    def find(self, val):
        for x in self.array[self.__hash(val)]:
            if x == val:
                return x
        return None

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
                self.add(x)

    # Generates a hash value in O(1) time. First it creates a hash from the given value by multiplying it by a
    # random 32 bit number, the getting the remainder of that divided by 2**32 (to throw away some of the bits),
    # then dividing by another large number to throw away more bits, creating a value that is within the size
    # of the backing array. The function is done again using the hashed value in place of the original value
    # to reduce collisions.
    def __hash(self, val):
        hashed_val = ((self.seed * int(val)) % 2 ** w) // 2 ** (w - self.dimension)
        return ((self.seed * hashed_val) % 2 ** w) // 2 ** (w - self.dimension)

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

    def __iter__(self):
        for elements in self.array:
            for x in elements:
                yield x
