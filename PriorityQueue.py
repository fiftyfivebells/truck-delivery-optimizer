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
        

    def is_empty(self):
        pass

    def enqueue(self, item):
        pass

    def dequeue(self):
        pass

    def peek(self):
        pass
