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
    
    for i in range(2, math.floor(math.sqrt(n))): # second arg not inclusive 
        if n % i == 0:
            return False
    return True

def is_prime_v2(n):

    return n > 1 and all(n % i != 0 for i in range(2, math.ceil(math.sqrt(n))))

def next_prime_v1(n):
    return n + 1 if is_prime_v2(n+1) else next_prime_v1(n+1)

def next_prime_v2(n):

    current_num = n+1
    
    while True:
        if is_prime_v2(current_num):
            return current_num
        else:
            current_num += 1

def test(num, func):
    start_time = datetime.datetime.now().time()

    result = func(num)

    end_time = datetime.datetime.now().time()

    datetimeFormat = '%H:%M:%S.%f'     
    timedelta = datetime.datetime.strptime(str(end_time), datetimeFormat) - datetime.datetime.strptime(str(start_time),datetimeFormat)

    return str(func) + ", " + str(result) + ", Total time:" + str(timedelta)


#test(1,is_prime_v2)

"""Testing start here"""


print("\n".join([test(100000000003,func) for func in [is_prime_v1, is_prime_v2]]))

print("\n".join([test(10000000,func) for func in [next_prime_v1, next_prime_v2]])) 


### Test 1
##start_time = datetime.datetime.now().time()
##
##print(is_prime_v0(test_num))
##
##end_time = datetime.datetime.now().time()
##
##datetimeFormat = '%H:%M:%S.%f'     
##timedelta = datetime.datetime.strptime(str(end_time), datetimeFormat) - datetime.datetime.strptime(str(start_time),datetimeFormat)
##
##print("Total time v0:", timedelta)
##
##
##
### Test 2
##print("\n************************************\n")
##start_time = datetime.datetime.now().time()
##
##print(is_prime_v1(test_num))
##
##end_time = datetime.datetime.now().time()
##
##datetimeFormat = '%H:%M:%S.%f'     
##timedelta = datetime.datetime.strptime(str(end_time), datetimeFormat) - datetime.datetime.strptime(str(start_time),datetimeFormat)
##
##print("Total time v1:", timedelta)
##
### Test 3
##print("\n************************************\n")
##start_time = datetime.datetime.now().time()
##
##print(is_prime_v2(test_num))
##
##end_time = datetime.datetime.now().time()
##
##datetimeFormat = '%H:%M:%S.%f'     
##timedelta = datetime.datetime.strptime(str(end_time), datetimeFormat) - datetime.datetime.strptime(str(start_time),datetimeFormat)
##
##print("Total time v2:", timedelta)



