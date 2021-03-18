import math
for n in range(1, 796):
    if ((pow(2, n) % 1000) + (pow(5, n) % 1000) - (n % 1000) == 0):
        print(n)
        break
