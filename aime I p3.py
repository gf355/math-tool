answerlist = []
ans = 0
for i in range(0, 12):
    for j in range(0, i):
        if (pow(2, i) - pow(2, j) < 1000):
            if (pow(2, i) - pow(2, j) not in answerlist):
                answerlist.append(pow(2, i) - pow(2, j))
                ans += 1
            else:
                print('Duplicate!')
answerlist.sort()
print(answerlist)
print(ans)