num = 0
tot = 0
for i in range(100, 1000):
    if ((i - (i % 100)) == (i % 10) * 100):
        tot = tot + i
        num += 1
print(tot)
print(num)
print(tot/num)
