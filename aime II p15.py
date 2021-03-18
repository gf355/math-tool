import math
def issqrt(num):
    root = math.sqrt(num)
    if int(root + 0.5) ** 2 == num:
        return True
    else:
        return False
def function1(a):
    if (issqrt(a) == True):
        return math.sqrt(a)
    else:
        return (1 + function1(a + 1))
def function2(b):
    if (issqrt(b) == True):
        return math.sqrt(b)
    else:
        return (2 + function2(b + 2))
for n in range(1, 1001):
    if (7 * function1(n) == 4 * function2(n)):
        print(n)
        break



