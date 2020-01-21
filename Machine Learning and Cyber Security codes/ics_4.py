import random

# method to get random prime numbers
def getPrimeNumbers():
    numbers = []
    for _ in range(2, 101):
        count = 0
        for __ in range(2, 101):
            if _ % __ == 0:
                count += 1
            elif count >= 2:
                break
        if count <= 1:
            numbers.append(_)
    print("The list of prime numbers from 1 to 100 :\n", numbers)
    return numbers


p, q = random.sample(getPrimeNumbers(), 2)
# p, q should be large prime numbers
# p = 79
# q = 97
print("The value of p :", p)
print("The value of q :", q)

# a,b should be large secret integers
a = 16
b = 25

R = (q**a) % p
S = (q**b) % p

print("The value of R :", R)
print("The value of S :", S)

Rk = (S**a) % p
Sk = (R**b) % p

print("The value of Rk :", Rk)
print("The value of Sk :", Sk)

if Rk == Sk:
    print("The keys generated are the same and hence, the encryption and decryption process can now begin")