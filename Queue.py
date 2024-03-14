# QUEUE IMPLEMENTATION
# DO NOT MODIFY

class Queue(object):
    def __init__(self, list=None):
        if list is None:
            list = []
        self.queue = list

#     def get_list(self):
#         return self.queue

    def size(self):
        return len(self.queue)

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def tail(self):
        return self.queue[-1]

    def deq(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)

    def enq(self, data=None):
        self.queue.append(data)

    def print(self):
        print(self.queue)

    def __str__(self):
        return self.queue.__str__()

    def __repr__(self):
        return self.queue.__repr__()

    def is_empty(self):
        return len(self.queue) == 0

    def clear(self):
        self.queue = []

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.queue == other.queue
        return False

def main():
    q = Queue()
    q.print()
    print("Is empty?", q.is_empty())
    for i in range(1, 7):
        q.enq(i)
    print("Front:   ", q.front())
    print("Deq:     ", q.deq())
    q.print()
    print("Is empty?", q.is_empty())

# Don't run main on import
if __name__ == "__main__":
    main()



