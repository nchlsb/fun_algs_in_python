# There are simpler ways to do this in Python, but this demos an algorithm 

def is_palindrome(string):

    i = 0
    j = len(string) - 1
    
    while i < j:
        if string[i] != string[j]: 
            return False        
        
        i += 1
        j -= 1

    return True

