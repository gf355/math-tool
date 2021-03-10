import math
# function to count the divisors 
def countDivisors(n) : 
    cnt = 0
    for i in range(1, (int)(math.sqrt(n)) + 1) : 
        if (n % i == 0) : 
              
            # If divisors are equal, 
            # count only one 
            if (n / i == i) : 
                cnt = cnt + 1
            else : # Otherwise count both 
                cnt = cnt + 2
                  
    return cnt 
def cubeRoot(x):
    return x ** (1./3.)
max = 0
ans = 0
for i in range(1, 100000):
    if (countDivisors(i) / cubeRoot(i)) > max:
        max = countDivisors(i) / cubeRoot(i)
        ans = i
print(ans)

