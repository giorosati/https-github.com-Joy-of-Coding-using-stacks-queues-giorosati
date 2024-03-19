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

    temp_string = "1"    # start the queue with a one
    temp.enq(temp_string)

    for i in range(1, N+1, 1):
        numbers.enq(temp_string)   # add to output queue
        temp_string = temp.deq()   # get top element from the temp queue
        
        if temp_string[-1] == "0":  # if last digit is a zero, change to a one
            temp_string = temp_string[:-1] + "1"
            # temp.enq(temp_string)
        
        elif len(temp_string) == 1:
                temp_string = "10"
        
        elif temp_string[-1] == "1":
            # need to find first prior zero. If all priors are 1, make string 1 + 0's
            zero_string = ""
            
            for j in range (0, len(temp_string), 1):
                if (temp_string[-(j+1)] == "1"):    # check if a this position is "1"
                    if j < len(temp_string):
                        zero_string = zero_string + "0" # add a zero for every "1" found
                        if j+1 == len(temp_string):
                            temp_string = temp_string = temp_string[:(-(j+1))] + "1" + zero_string
                    
                else:
                    temp_string = temp_string[:(-(j+1))] + "1" + zero_string 
                    break

        temp.enq(temp_string)    

    return numbers  # return the queue

def main():
    generate_binary_numbers(2).print()
    generate_binary_numbers(3).print()
    generate_binary_numbers(6).print()
    # generate_binary_numbers(10).print()


# Don't run main on import
if __name__ == "__main__":
    main()

