# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 1: REVERSE QUEUE
#
# NAME:         Giovanni Rosati
# DATE:         2024-03-14
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue
from Stack import Stack


# Return a new queue in reverse order
# Hint: can use a stack to help
def reverse(q_orig):
    q_new = Queue([])
    s_temp = Stack([])

    while not q_orig.is_empty():
        # print("executing deq")
        s_temp.push(q_orig.deq())
    
    while not s_temp.is_empty():
        # print("executing enq")
        q_new.enq(s_temp.pop())

    return q_new

def main():
    q = Queue(list(range(1, 5)))
    q.print()
    print("reverse: ", end="")
    reverse(q).print()

# Don't run main on import
if __name__ == "__main__":
    main()
