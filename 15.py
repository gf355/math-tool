import math
from math import comb
ans = 0
for i in range(0, 7):
    for j in range(0, 9):
        if (abs(i - j) % 4 == 0) and (i + j >= 1):
            ans += comb(6, i) * comb(8, j)
            print(i, end = ' ')
            print(j)
print(ans)

