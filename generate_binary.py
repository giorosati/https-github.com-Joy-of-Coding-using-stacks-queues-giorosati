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
    temp_queue = Queue([])

    if N < 1: return numbers

    temp_queue.enq("1")
    string1 = ""

    count = 0

    for i in range(N):
        # while not temp_queue.is_empty():
        #     string1 = temp_queue.deq() + string1
        temp_char = temp_queue.deq()
        if temp_char == "0":     # when least sig. bit is zero, replace it with a 1
            temp_queue.enq("1")
        else:
            temp_queue.deq()       #remove last "1"
            count += 1
            size = temp_queue.size()    # get size of temp_queue
            for i in range(-1, -size, -1):   #iterate backwards from end of queue
                # find the first occurrance of a zero, iterating backwards
                temp_digit = temp_queue.deq()   # get next digit
                count += 1
                if temp_digit == "0": 
                    temp_queue.enq("1")   # zero found, change to 1
                    for i in range(0, count-1, 1):    # add zeros after
                        temp_queue.enq("0")



        # create string to numbers queue
        while not temp_queue.is_empty():
            string1 = temp_queue.deq() + string1

        # add string to numbers queue
        numbers.enq(string1)


    
    return numbers

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()

