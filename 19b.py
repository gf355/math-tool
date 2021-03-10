minans = 100
aans = 0
bans = 0
def fun(m, n):
    sum7 = 0
    sum10 = 0
    sum12 = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i + j == 7:
                sum7 += 1
            elif i + j == 10:
                sum10 += 1
            elif i + j == 12:
                sum12 += 1
    if (sum7 * 4 == sum10 * 3) and (sum12 * 12 == m * n):
        return True
    else:
        return False
for a in range(6, 20):
    for b in range(6, 20):
        if fun(a, b) == True:
            if a + b < minans:
                minans = a + b
                aans = a
                bans = b
print(minans)
print(aans)
print(bans)