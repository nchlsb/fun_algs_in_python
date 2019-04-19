# https://en.wikipedia.org/wiki/Primality_test#Pseudocode as Python and time interval to test large numbers

import datetime

def is_prime(n):
    
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

# Test(s) start here
start_time = datetime.datetime.now().time()

print(is_prime(5915587277))

end_time = datetime.datetime.now().time()

datetimeFormat = '%H:%M:%S.%f'     
timedelta = datetime.datetime.strptime(str(end_time), datetimeFormat) - datetime.datetime.strptime(str(start_time),datetimeFormat)

print("Start time: ", start_time)
print("End time: ", end_time)
print("Total time:", timedelta)


