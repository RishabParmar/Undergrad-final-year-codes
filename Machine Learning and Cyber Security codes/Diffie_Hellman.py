import random


def gettingRandomPrimeNumbers():
    prime_numbers = []
    for num in range(2, 101):
        flag = 0
        for _ in range(2, 101):
            if num == _:
                break
            elif (num % _) == 0:
                flag = 1
        if flag == 0:
            prime_numbers.append(num)
    print("The prime numbers are :", prime_numbers)
    return random.sample(prime_numbers, 2)


# Selecting two large prime numbers
# p = 7
# q = 17
p, q = gettingRandomPrimeNumbers()
print("The value of p: %d and q: %d" % (p, q))
print("The value of q:", q)
# Selecting two large secret random integers (a is related to R and b is related to S)
# a = 6
# b = 4
a, b = random.sample(list(range(1, 100)), 2)
print("The value of a :", a)
print("The value of b :", b)
# Calculating the value of R and S
R = (q**a) % p
S = (q**b) % p
print("The value of R :", R)
print("The value of S :", S)
# Calcualting the secret keys Rk and Sk
Rk = (S**a) % p
Sk = (R**b) % p
print("The secret key Rk : ", Rk)
print("The secret key Sk : ", Sk)
if Rk == Sk:
    k = Rk
    print("The Key obtained from Diffie Hellman Algorithm :", k)
else:
    print("The keys cannot be exchanged")
