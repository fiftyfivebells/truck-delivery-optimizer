class PQItem(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority

# Returns the left child of given index
def left(i):
    return 2*i + 1

# Returns right child of given index
def right(i):
    return 2*(i + 1)

# Returns parent of given index
def parent(i):
    return (i - 1) // 2


class PriorityQueue(object):
    def __init__(self):
        self.array = [[] for _ in range(2)]
        self.size = 0

    def is_empty(self):
        return self.size == 0

    # Adds element in O(log n) time. Puts new element in the last spot of the
    # backing array and "bubbles" it up, swapping with its parent as long as
    # it has a higher priority. Will resize the backing array if the number of
    # items in the queue is equal to the length of the array
    def enqueue(self, item, priority):
        if len(self.array) < self.size + 1:
            self.__resize()

        to_add = PQItem(item, priority)

        self.array[self.size] = to_add
        self.size += 1
        self.__bubble_up(self.size - 1)
        return True

    # Removes an element in O(log n) time. Takes the element out of the 0th index
    # of the backing array, then puts the last element in the backing array in its
    # spot. Then it "trickles" the moved element down until it is a lower priority
    # than it's parent, but higher than its children
    def dequeue(self):
        if self.size == 0:
            raise IndexError
        removed = self.array[0]
        self.array[0] = self.array[self.size - 1]
        self.size -= 1

        self.__trickle_down(0)
        if 3*self.size < len(self.array):
            self.__resize()

        return removed.item

    # Returns the top element in the queue, but does not remove it. Completes in
    # O(1) time because it's an array lookup.
    def peek(self):
        if self.size == 0:
            raise IndexError()
        return self.array[0]

    def __resize(self):
        new_size = max(2*self.size, 1)
        new_arr = [[] for _ in range(new_size)]

        for i in range(self.size):
            new_arr[i] = self.array[i]

        self.array = new_arr

    # Takes the last item in the backing array and "bubbles" it up, swapping
    # with the parent as long as the parent has a lower priority. Stops looping
    # when the item is a lower priority than its parent. Completes in O(log n).
    def __bubble_up(self, i):
        p = parent(i)
        while i > 0 and self.array[i].priority < self.array[p].priority:
            self.array[i], self.array[p] = self.array[p], self.array[i]
            i = p
            p = parent(i)

    # Forces an element down as long as it has a lower priority than its child
    # nodes. Stops looping as soon as the child has lower priority than the
    # item we're comparing. Completes in O(log n) time.
    def __trickle_down(self, i):
        while i >= 0:
            j = -1
            r = right(i)
            if r < self.size and self.array[r].priority < self.array[i].priority:
                l = left(i)
                if self.array[l].priority < self.array[r].priority:
                    j = l
                else:
                    j = r

            else:
                l = left(i)
                if l < self.size and self.array[l].priority < self.array[i].priority:
                    j = l

            if j >= 0:
                self.array[j], self.array[i] = self.array[i], self.array[j]

            i = j
