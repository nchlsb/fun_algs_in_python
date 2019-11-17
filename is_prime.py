import datetime
import math 

"""The first method is heuristic. The second two demo replacing syntax"""

def is_prime_v0(n):
    
    if n <= 3:
        return n > 1
    
    elif n%2 == 0 or n % 3 == 0:
        return False
    
    i = 5

    while i * i <= n:
        
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True

def is_prime_v1(n):
    
    for i in range(2, math.floor(math.sqrt(n)) + 2): # second arg not inclusive 
        if n % i == 0:
            return False
    return True

def is_prime_v2(n):

    return n > 1 and all(n % i != 0 for i in range(2, math.floor(math.sqrt(n))))


"""Tets start here"""
"""Future thoughts: make the test itself into a function in order to repeat w/o hard coding?"""

#test_num = 101740496633 
test_num = 5915587277

# Test 1
start_time = datetime.datetime.now().time()

print(is_prime_v0(test_num))

end_time = datetime.datetime.now().time()

datetimeFormat = '%H:%M:%S.%f'     
timedelta = datetime.datetime.strptime(str(end_time), datetimeFormat) - datetime.datetime.strptime(str(start_time),datetimeFormat)

print("Total time v0:", timedelta)



# Test 2
print("\n************************************\n")
start_time = datetime.datetime.now().time()

print(is_prime_v1(test_num))

end_time = datetime.datetime.now().time()

datetimeFormat = '%H:%M:%S.%f'     
timedelta = datetime.datetime.strptime(str(end_time), datetimeFormat) - datetime.datetime.strptime(str(start_time),datetimeFormat)

print("Total time v1:", timedelta)

# Test 3
print("\n************************************\n")
start_time = datetime.datetime.now().time()

print(is_prime_v2(test_num))

end_time = datetime.datetime.now().time()

datetimeFormat = '%H:%M:%S.%f'     
timedelta = datetime.datetime.strptime(str(end_time), datetimeFormat) - datetime.datetime.strptime(str(start_time),datetimeFormat)

print("Total time v2:", timedelta)



