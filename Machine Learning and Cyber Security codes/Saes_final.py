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


def XOR(temp1, temp2):
    result = int(temp1, 16) ^ int(temp2, 16)
    return hex(result)[2:]


def subNibble(input, box):
    number = bin(int(input, 16))[2:].zfill(4)
    row = int(number[0]+number[1], 2)
    column = int(number[2]+number[3], 2)
    return box[row][column]


def genT(input, rc):
    t0 = subNibble(input[0], S)
    t1 = subNibble(input[1], S)
    # rotate
    total = t1 + t0
    return XOR(total, rc)


def generateKeys(k):
    sk = []
    w = [0] * 6
    k = hex(int(k.replace(" ", ''), 2))[2:]
    # 24
    w[0] = k[: 2]
    # 75
    w[1] = k[2:]
    sk.append(w[0] + w[1])
    t2 = genT(w[1], rc1)
    w[2] = XOR(t2, w[0])
    print("The value of w2 :", w[2])
    w[3] = XOR(w[1], w[2])
    print("The value of w3: ", w[3])
    sk.append(w[2] + w[3])
    t4 = genT(w[3], rc2)
    print("The value of t4: ", t4)
    print("The value of w2----: ", w[2])
    w[4] = XOR(t4, w[2])
    print("The value of w4: ", w[4])
    w[5] = XOR(w[3], w[4])
    sk.append(w[4] + w[5])
    return sk


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


def mixCol(state):
    s00 = XOR(mult(1, state[0]), mult(4, state[1]))
    s10 = XOR(mult(4, state[0]), mult(1, state[1]))
    s01 = XOR(mult(1, state[2]), mult(4, state[3]))
    s11 = XOR(mult(4, state[2]), mult(1, state[3]))
    return s00 + s10 + s01 + s11


def mixCol_inv(state):
    s00 = XOR(mult(9, state[0]), mult(2, state[1]))
    s10 = XOR(mult(2, state[0]), mult(9, state[1]))
    s01 = XOR(mult(9, state[2]), mult(2, state[3]))
    s11 = XOR(mult(2, state[2]), mult(9, state[3]))
    return s00 + s10 + s01 + s11


def subNibbles(state, box):
    result = ""
    for _ in state:
        result += subNibble(_, box)
    return result


def shiftRows(input):
    return input[0] + input[3] + input[2] + input[1]


def encrypt(plain_t, keys):
    plain_t = hex(int(plain_t.replace(" ", ''), 2))[2:]
    print("The original plain text :", plain_t)

    temp = XOR(plain_t, keys[0])
    print("Pre :", temp)

    temp = shiftRows(temp)
    print("Shift rows :", temp)
    temp = subNibbles(temp, S)
    print("Sub nibbles :", temp)
    temp = mixCol(temp)
    print("Mix Columns :", temp)
    temp = XOR(temp, keys[1])

    temp = shiftRows(temp)
    print("Shift rows :", temp)
    temp = subNibbles(temp, S)

    temp = XOR(temp, keys[2])
    return temp


def decrypt(cipher_t, keys):

    temp = XOR(cipher_t, keys[2])
    print("1 :", temp)

    temp = subNibbles(temp, Si)
    print("2 :", temp)
    temp = shiftRows(temp)
    print("3 :", temp)
    temp = XOR(temp, keys[1])
    print("4 :", temp)

    temp = mixCol_inv(temp)
    print("The value after mix col _inv :", temp)
    temp = subNibbles(temp, Si)
    print("5 :", temp)
    temp = shiftRows(temp)
    print("6 :", temp)

    temp = XOR(temp, keys[0])
    print("7 :", temp)

    return temp


# Key generation
keys = generateKeys(key)
print("The keys generated are: ", keys)
cipher = encrypt(pt, keys)
print("The cipher text :", cipher)
plain_text = decrypt(cipher, keys)
print("The original plain text :", plain_text)
