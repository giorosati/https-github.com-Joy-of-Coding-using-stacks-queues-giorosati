# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 4: COUNT THE LONGEST SUBSEQUENCE
#
# NAME:         Giovanni Rosati
# DATE:         2024-03-21
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# count longest sequence of duplicates in a queue
# can destroy the queue & make it empty
def count_longest(q):
    len = 0
    temp_len = 0
    if q.size() == 0:
        return 0
    elif q.size() == 1:
        return 1
    else:
        temp1 = q.deq()
        temp_len += 1
    while q.size() > 0:
        temp2 = q.deq()
        if temp2 == temp1:
            temp_len += 1
        else:
            temp1 = temp2
            if temp_len > len: 
                len = temp_len
            if q.size() > 0: temp_len = 1
    if temp_len > len: 
                len = temp_len
    return len

def main():
    print("out 2:", count_longest(Queue([l for l in "hello"])))
    print("out 5:", count_longest(Queue([l for l in "m" * 5])))
    print("out 3:", count_longest(Queue([l for l in "heee" ])))



# Don't run main on import
if __name__ == "__main__":
    main()

