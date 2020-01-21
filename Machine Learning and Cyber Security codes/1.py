key = "0010 0100 0111 0101"  # 16 bit
pt = '1001 0100 0010 0111'
rc1 = '80'
rc2 = '30'

S = [['9', '4', 'A', 'B'],
     ['D', '1', '8', '5'],
     ['6', '2', '0', '3'],
     ['C', 'E', 'F', '7']]

Si = [['A', '5', '9', 'B'],
      ['1', '7', '8', 'F'],
      ['6', '0', '2', '3'],
      ['C', '4', 'D', 'E']]


def XOR(list1, list2):
    result = int(list1, 16) ^ int(list2, 16)
    return hex(result)[2:]


def subNibble(input, box):
    result = bin(int(input, 16))[2:].zfill(4)
    row = int(result[0] + result[1], 2)
    column = int(result[2] + result[3], 2)
    return box[row][column]


def genT(input, rc):
    t0 = subNibble(input[0], S)
    t1 = subNibble(input[1], S)
    total = t1 + t0
    return XOR(total, rc)


def generateKeys(plain_text):
    subkeys = []
    w = [0] * 6
    k = hex(int(plain_text.replace(" ", ""), 2))[2:]
    w[0] = k[:2]
    print("The value of w :", w[0])
    w[1] = k[2:]
    print("The value of w :", w[1])
    subkeys.append(w[0] + w[1])
    t2 = genT(w[1], rc1)
    print("The value of t2: ", t2)
    w[2] = XOR(w[0], t2)
    print("The value of w2: ", w[2])
    w[3] = XOR(w[2], w[1])
    print("The value of w3: ", w[3])
    subkeys.append(w[2] + w[3])
    t4 = genT(w[3], rc2)
    print("The value of t4: ", t4)
    w[4] = XOR(w[2], t4)
    print("The value of w4: ", w[4])
    w[5] = XOR(w[3], w[4])
    subkeys.append(w[4] + w[5])
    return subkeys


def shiftRows(temp):
    return temp[0] + temp[3] + temp[2] + temp[1]


def subNibbles(temp, box):
    result = ""
    for _ in temp:
        result += subNibble(_, box)
    return result


def mult(num, h):
    h = int(h, 16)
    val = num * h
    if num != 9:
        if val >= 64:
            val ^= 76
        if val >= 32:
            val ^= 38
        if val >= 16:
            val ^= 19
    else:
        val = 8 * h
        if val >= 64:
            val ^= 76
        if val >= 32:
            val ^= 38
        if val >= 16:
            val ^= 19
        val ^= h
    return hex(val)[2:]


def mixCols(temp):
    s00 = XOR(mult(1, temp[0]), mult(4, temp[1]))
    s10 = XOR(mult(4, temp[0]), mult(1, temp[1]))
    s01 = XOR(mult(1, temp[2]), mult(4, temp[3]))
    s11 = XOR(mult(4, temp[2]), mult(1, temp[3]))
    return s00 + s10 + s01 + s11


def mixCols_inv(temp):
    s00 = XOR(mult(9, temp[0]), mult(2, temp[1]))
    s10 = XOR(mult(2, temp[0]), mult(9, temp[1]))
    s01 = XOR(mult(9, temp[2]), mult(2, temp[3]))
    s11 = XOR(mult(2, temp[2]), mult(9, temp[3]))
    return s00 + s10 + s01 + s11


def encrypt(inp):
    temp = ""
    print("The original plain text :", hex(int(inp.replace(" ", ""), 2))[2:])
    temp = hex(int(inp.replace(" ", ""), 2))[2:]

    temp = XOR(temp, keys[0])

    temp = shiftRows(temp)
    temp = subNibbles(temp, S)
    temp = mixCols(temp)
    temp = XOR(temp, keys[1])

    temp = shiftRows(temp)
    temp = subNibbles(temp, S)
    temp = XOR(temp, keys[2])

    return temp


def decrypt(inp):
    temp = XOR(inp, keys[2])

    temp = shiftRows(temp)
    temp = subNibbles(temp, Si)
    temp = XOR(temp, keys[1])

    temp = mixCols_inv(temp)
    temp = shiftRows(temp)
    temp = subNibbles(temp, Si)
    temp = XOR(temp, keys[0])

    return temp


# keyGeneration
keys = generateKeys(key)
print("The keys generated are :", keys)

# Encryption
cipher_text = encrypt(pt)
print("The original cipher text :", cipher_text)
# Decryption
plain_txt = decrypt(cipher_text)
print("The original plain text :", plain_txt)
