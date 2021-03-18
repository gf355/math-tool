def hcfnaive(a,b): 
    if(b==0): 
        return a 
    else: 
        return hcfnaive(b,a%b)
num = 0
for m in range(1, 31):
    for n in range(1, 31):
        if (m != n):
            a = pow(2, m) + 1
            b = pow(2, n) - 1
            if (hcfnaive(a,b) != 1):
                num += 1
print(num)
