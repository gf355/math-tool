ans = 0
for a in range(1, 6):
    for b in range(1, 6):
        for c in range(1, 6):
            for d in range(1, 6):
                for e in range(1, 6):
                    if (a != b and a != c and a != d and a != e and b != c and b != d and b != e and c != d and c != e and d != e):
                        if ((a * b * c + b * c * d + c * d * e + d * e * a + e * a * b) % 3 == 0):
                            ans += 1
print(ans)
