def getTheValueOfPrivateKey(g, c):
    for _ in range(0, 20):
        if ((g * _) + 1) % c == 0:
            return int(((g * _) + 1) / c)


def getTheValueOfPublicKey(x, y):
    while y != 0:
        r = x % y
        x = y
        y = r
    return x


a = 13
b = 11

# Calculating n
n = a * b
print("The value of n :", n)

# Calculating n-1
f_n = (a - 1) * (b - 1)
print("The value of f_n :", f_n)

# Calculating e
for _ in range(2, f_n):
    e = getTheValueOfPublicKey(f_n, _)
    if e == 1:
        e = _
        break
print("The value of e :", e)

# Calculating d
d = getTheValueOfPrivateKey(f_n, e)
print("The value of d :", d)

# Cipher text
P = 122
C = (P**e) % n
print("The cipher text :", C)

# Plain text
P = (C**d) % n
print("The original plain text :", P)
