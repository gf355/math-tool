x = -50.0
y = -50.0
min = 1000.0 
while x < 50:
    while y < 50: 
        if pow(x * y - 1, 2) + pow(x + y, 2) < min:
            min = pow(x * y - 1, 2) + pow(x + y, 2)
        y += 0.1
    x += 0.1
print(min)

