import math
def isp(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
number = int(input('Enter a number:\n'))
if isp(number) == True:
    print(f'{number} is a prime.')
else:
    print(f'{number} is NOT a prime.')
