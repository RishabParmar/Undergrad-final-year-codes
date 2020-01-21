def computeTheValueOfPublicKey(f_n, public_key):
    for num in range(0, 50):
        value = ((f_n * num) + 1) % public_key
        if value == 0:
            return ((f_n * num) + 1)/public_key


# Euclid's method to find the GCD
def computeTheValueOfe(num, f_n):
    while num != 0:
        r = f_n % num
        f_n = num
        num = r
    return f_n


# a and b are the random prime numbers where a != b
# Consider only small numbers
a = 3
b = 7

# Computing n
n = a * b
print("The value of n :", n)

# Computing f(n)
function_of_n = (a-1) * (b-1)
print("The value of f(n) :", function_of_n)

# e = public key (used for encryption) and d = private key (used for decryption)
for num in range(2, function_of_n):
    e = computeTheValueOfe(num, function_of_n)
    if e == 1:
        e = num
        break
print("The value of public key :", e)

# Computing d
d = computeTheValueOfPublicKey(function_of_n, e)
print("The value of private key : ", d)

# You can directly use the plain_text = 6 an integer
plain_text_message = "00011000"
# Converting the plain_text from binary to decimal form
plain_text = int(plain_text_message, 2)
print("The plain text in binary form : ", plain_text)

# Encryption
cipher_text = (3**e) % n
print("The cipher text :", cipher_text)

# Decryption
plain_text = (cipher_text**d) % n
print("The value of plain text :", plain_text)
