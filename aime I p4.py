ans = 0
for i in range(1, 67):
    for j in range(i+1, 67):
        for k in range(j+1, 67):
            if (i + j + k == 66):
                print(i , j , k )
                ans += 1
print(ans)