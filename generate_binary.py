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
    temp = Stack([])

    if N < 1: return numbers

    temp.push(1)

    for i in range(N):
        temp_string = str(temp.pop())
        numbers.enq(temp_string)
        for j in range (-1, -len(temp_string), -1):
            if temp_string[j] == "0":     # 
                temp_string[j]=("1")
                break
            elif:
                if j == len(temp_string):
                    
            count += 1
    



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

