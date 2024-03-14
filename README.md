# Project 2: Stacks & Queues
Please complete the following 4 functions. You can test by running the `pytest` or `python3` commands:

* To run just the main code for one problem: `python3 reverse.py`
* To run the tests for one problem: `pytest reverse_test.py`
* To run all the tests prior to submission: `pytest`

### Files that should (& shouldn't!) be changed

You **SHOULD** implement your problem solutions in the following files:
* reverse.py
* matching.py
* generate_binary.py
* count_longest.py

You **SHOULD NOT** modify the following files:
* Queue.py
* Stack.py
* count_longest_test.py
* generate_binary_test.py
* matching_test.py
* reverse_test.py

Looking for additional practice problems to prepare for the exam?
* practice-problems.py

### General Hints
* _Thinking of using a loop? For loops are for strings, whiles are for Stacks & Queues!_
* _The only way to iterate / loop through the Stack or Queue you've been given in this assignment is to destroy it (i.e., make it empty)._
* _You should only be accessing the functions of Queue & Stack, not the underlying lists._

## Problem 1: reverse queue

Write a function ```reverse``` in python that takes a
queue as a parameter and returns a new queue in 
reverse order. Your solution _should not_ use
any built-in or library functions other than those in
the `Stack` and `Queue` classes provided.

| **Example call** | **Returns** |
| -------------- | --------- |
| `reverse( Q[1, 2, 3, 4] )` | `Q[4, 3, 2, 1]` |
| `reverse( Q[hello] )` | `Q[olleh]` |
| `reverse( Q[0] )` | `Q[0]` |

_Note:_ We are using the notation `Q[ ]` here to 
differentiate our queues from lists or arrays.

_**Hint**: use a stack to help! You can destroy the queue & make it empty!_

## Problem 2: brace matcher

Write a function `matcher` in python that takes a
string containing braces (`[{()}]`) as a parameter
and returns True if the braces are matched, and
False otherwise. The braces may be nested. 
Your solution _should not_ use
any built-in or library functions other than those in
the `Stack` and `Queue` classes provided.

| **Example call** | **Returns** |
| -------------- | --------- |
| `matcher("[()]")` | `True` |
| `matcher("[(")` | `False` |
| `matcher("hello")` | `True` |

_**Hint**: use a stack! And make sure the braces **MATCH**!_

_**Hint 2**: consider making your code DRYer by using a dictionary to determine if an open or closed brace matches. (For full credit, **DO NOT** use the dictionary in place of the stack to determine overall matching.)_

## Problem 3: generate binary number strings

Write a function ```generate_binary_numbers``` that
takes a number _N_ as a parameter and returns a queue
of binary number strings from _1_ to _N_ _without_ 
using any built-in or library functions like `bin()`. 
In fact, your solution _should not_ use
any built-in or library functions other than those in
the `Stack` and `Queue` classes provided.
The front of the queue begins @ '1'. If _N_ is too 
small, return an empty queue. A successful solution
does **not** calculate binary numbers mathematically
but __only__ adds strings together.

| **Example call** | **Returns** |
| -------------- | --------- |
| `generate_binary_numbers(2)` | `Q['1', '10']` |
| `generate_binary_numbers(3)` | `Q['1', '10', '11']` |
| `generate_binary_numbers(6)` | `Q['1', '10', '11', '100', '101', '110']` |

_**Hint**: use an extra queue to help! Start from 1, & add 0 & 1 to copies of it._

### Algorithm Overview
```
1) Create two empty queues of strings: a temp one & one to return 
2) Enqueue the first binary number "1" to the temp queue. 
3) Now run a loop for generating and creating a queue of n binary numbers. 
......a) Dequeue the front of the temp queue & add it to the output queue (to be returned). 
......b) Append "0" at the end of the dequeued front item and enqueue it to the temp queue. 
......c) Append "1" at the end of the dequeued front item and enqueue it to the temp queue.
```
Algorithm adapted from https://www.geeksforgeeks.org/interesting-method-generate-binary-numbers-1-n/


### Review: Binary Numbers

Recall that the typical numbers we are used to
working with every day are decimal numbers, or
base 10. By contrast, computers  natively work
with _**binary numbers**_, which are base 2.

To read binary numbers, begin writing the powers
of 2 from right to left:

| **Binary** | **Decimal** |
| -------------- | --------- |
|2<sup>3</sup> 2<sup>2</sup> 2<sup>1</sup> 2<sup>0</sup> | |
| `8 4 2 1` | |
| `. . . 1` | 1 |
| `. . 1 0` | 2 |
| `. . 1 1` | 3 |
| `. 1 0 0` | 4 |
| `. 1 0 1` | 5 |
| `. 1 1 0` | 6 |
| `. 1 1 1` | 7 |
| `1 0 0 0` | 8 |
| `1 1 0 0` | 12 |
| `1 1 1 1` | 15 |

_Note:_ The dots (`.`) should **not** be in your final
output, but are used here to align the numbers under
the appropriate power of 2.

## Problem 4: count the longest subsequence

Write a function ```count_longest``` that takes a
queue of characters as a parameter and returns the
length of the longest consecutive subsequence. For
example:

| **Example call** | **Returns** |
| -------------- | --------- |
| `count_longest( Q[h, e, l, l, o] )` | `2` |
| `count_longest( Q[m, m, m, m, m] )` | `5` |
| `count_longest( Q[h, e, e, e] )` | `3` |
| `count_longest( Q[ ] )` | `0` |

_**Hint**: you can destroy the queue & make it empty!_

Your solution _should not_ use
any built-in or library functions other than those in
the `Stack` and `Queue` classes provided.

## Getting started

### Develop in an IDE
 
You will need to install PyCharm (or another IDE),
git, and pytest. PyCharm has some built-in git 
support.

## Testing
Many of the tests are failing right now because the 
functions
aren't outputting the correct information. Fixing this
will make the tests pass & turn green.

### Setup

#### repl.it or command line
To use pytest on repl.it, install it first:

`pip3 install pytest`

To install pytest on the command line for running on a laptop (using a linux or unix based command-line like MacOS):

`sudo -H pip3 install pytest`

#### Pycharm
If using PyCharm, you may need to fix your project setup.
- Open the **Settings/Preferences | Tools | Python Integrated Tools** settings dialog.
- In the Default test runner field select **pytest**.
- Click OK to save the settings.

#### VS Code
If using VS Code, you may need to configure your pytest settings.
- Open a python (.py) file
- In the testing panel, select the **Configure Pytests** button
- Select **.root** directory for the testing route
- Refresh the panel if needed if tests are not discovered

### Run commands
To run just the main code for one problem:

`python3 reverse.py`

To run the tests for one problem:

`pytest reverse_test.py`

To run all the tests prior to submission:

`pytest`
