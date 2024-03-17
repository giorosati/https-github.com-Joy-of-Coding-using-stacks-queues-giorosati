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
# ......c) Append "1" at the end of the dequeued front item and enqueue it to the temp queue.
# Algorithm adapted from https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/

def generate_binary_numbers(N):
    numbers = Queue([])  # final queue to be returned
    temp = Queue([])     # temp queue to build strings representing each binary number

    if N < 1: return numbers    # returns empty queue if argument is less than one

    temp.enq("1")    # start the queue with a one
    

    for i in range(1, N, 1):
    
        temp_string = temp.deq()   # get top element from the temp queue
        numbers.enq(temp_string)   # add to output queue
        
        if temp_string[-1] == "1":
            temp_string = temp_string + "0"
            temp.enq(temp_string)

        elif temp_string[-1] == "0":
            temp_string = temp_string + "1"
            temp.enq(temp_string)


        # temp.enq(temp1_string)




        
        # numbers.enq(temp_string)
        # for j in range (-1, -len(temp_string), -1):
        #     if temp_string[j] == "0":     # 
        #         temp_string[j]=("1")
        #         break

        #     temp.enq("0")  # if a 0 was not found, add a  0 to the queue

        #     if -j == len(temp_string):   #iteration has reached the beginning of the string
        #         while not temp.is_empty():
        #             temp_string = temp_string + temp.deq()

            
        #     # add string to numbers queue            
        # numbers.enq(temp_string)
            
    
    return numbers  # return the queue

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()


# Don't run main on import
if __name__ == "__main__":
    main()

