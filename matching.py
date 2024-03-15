# MODIFY ME TO IMPLEMENT YOUR SOLUTION
# TO PROBLEM 2: BRACE MATCHER
#
# NAME:         Giovanni Rosati
# DATE:         2024-03-14
# ASSIGNMENT:   Project 2: Stacks & Queues

from Stack import Stack

# Returns True if the braces match,
# & False otherwise
def matcher(str):
    s_paren = Stack([])  #stack for ()
    s_braces = Stack([]) # stack for []
    s_curly = Stack([])  # stack for {}
    s_last_open = Stack([])  # stack to track order of open side elements
    
    for element in str:
        if element == "(":
            s_paren.push(element)
            s_last_open.push(element)

        elif element == "[": 
            s_braces.push(element)
            s_last_open.push(element)

        elif element == "{": 
            s_curly.push(element)
            s_last_open.push(element)


        elif element == ")":
            if s_last_open.peek() != "(": return False
            s_last_open.pop()
            s_paren.pop()
        
        elif element == "]":
            if s_last_open.peek() != "[": return False
            s_last_open.pop()
            s_braces.pop()
            
        elif element == "}":
            if s_last_open.peek() != "{": return False
            s_last_open.pop()
            s_curly.pop()

    if s_paren.is_empty() and s_braces.is_empty() and s_curly.is_empty():
        return True
    else:
        return False

def main():
    print("matcher: ", matcher("[()]"))

# Don't run main on import
if __name__ == "__main__":
    main()

