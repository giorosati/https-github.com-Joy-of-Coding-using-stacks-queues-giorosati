# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 3: GENERATE BINARY NUMBER STRINGS
#
# NAME:         Giovanni Rosati
# DATE:         2024-03-14
# ASSIGNMENT:   Project 2: Stacks & Queues

from Queue import Queue

# generate & return a queue of binary number strings from 1 to N
# front of queue begins @ '1', returns empty Queue otherwise

# from readme
### Algorithm Overview

# 1) Create two empty queues of strings: a temp one & one to return 
# 2) Enqueue the first binary number "1" to the temp queue. 
# 3) Now run a loop for generating and creating a queue of n binary numbers. 
# ......a) Dequeue the front of the temp queue & add it to the output queue (to be returned). 
# ......b) Append "0" at the end of the dequeued front item and enqueue it to the temp queue. 
# ......c) Append "1" at the end of the dequeued front item and enqueue it to the temp queue.Algorithm adapted from https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/

def generate_binary_numbers(N):
    numbers = Queue([])
    temp = Queue([])

    if N < 1: return numbers

    temp.enq(1)

    for i in range(N):


        numbers.enq(temp.deq)


    
    return numbers

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()

