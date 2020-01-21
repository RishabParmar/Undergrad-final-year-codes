def mixColumns(input):
    final = []
    mix_columns_code = [[0, 0, 0, 0], [0, 1, 0, 0], [1, 0, 0, 0], [1, 1, 0, 0],
                        [0, 0, 1, 1], [0, 1, 1, 1], [1, 0, 1, 1], [1, 1, 1, 1],
                        [0, 1, 1, 0], [0, 0, 1, 0], [1, 1, 1, 0], [1, 0, 1, 0],
                        [0, 1, 0, 1], [0, 0, 0, 1], [1, 1, 0, 1], [1, 0, 0, 1]]
    Me_table = [[1, 4],
                [4, 1]]
    result = list(input)
    result = [[result[0:4], result[4:8]],
              [result[8:12], result[12:]]]
    for i in range(0, 2):
        for j in range(0, 2):
            temp = []
            for k in range(0, 2):
                t1 = Me_table[i][k]
                t2 = result[k][j]
                if t1 == 1:
                    temp.append(t2)
                else:
                    index = int(str(t2[0])+str(t2[1])+str(t2[2])+str(t2[3]), 2)
                    temp.append(mix_columns_code[index])
            final += (XOR(temp[0], temp[1]))
    return final


def shiftRows(input):
    temp = list(input)
    temp = temp[0:4] + temp[12:] + temp[8:12] + temp[4:8]
    return temp


def XOR(list1, list2):
    temp = []
    for _ in range(0, len(list1)):
        temp.append(list1[_] ^ list2[_])
    return temp


def convertTheStringIntoListOfInteger(str):
    temp = []
    for _ in str:
        temp.append(int(_))
    return temp


def rotateNibble(input):
    temp = list(input)
    temp = temp[4:] + temp[0:4]
    print("The output of rotateNibble :", temp)
    return temp


def subNibble(input):
    sbox = [[9, 4, 10, 11],
            [13, 1, 8, 5],
            [6, 2, 0, 3],
            [12, 14, 15, 7]]
    temp = list(input)
    positions = []
    count = 0
    for _ in range(0, 4):
        positions.append(int(str(temp[count]) + str(temp[count + 1]), 2))
        count += 2
    index1 = sbox[positions[0]][positions[1]]
    index2 = sbox[positions[2]][positions[3]]
    # index1 = 1 or index2 =7, now bin will give 0b111 for index2, then replace gives 111 and zfill pads or adds zeros
    # to the string obtained from replace i.e. 0111 will be the result. Similarly for index1 = 1, we get the result as
    # 0001. The methods work in the following way from left to right, after binary output we get replaced output and
    # finally zfill gives the final string which we convert into list of intergers but calling the
    # convertTheStringIntoListOfIntegers().
    sublist1 = convertTheStringIntoListOfInteger(bin(index1).replace("0b", "").zfill(4))
    sublist2 = convertTheStringIntoListOfInteger(bin(index2).replace("0b", "").zfill(4))
    return sublist1 + sublist2


def keyGeneration(k):
    round_constant_0 = [1, 0, 0, 0, 0, 0, 0, 0]
    round_constant_1 = [0, 0, 1, 1, 0, 0, 0, 0]
    generated_keys = []
    temp_key = list(k)
    w0, w1 = [temp_key[0:8], temp_key[8:]]
    print("w0: ", w0)
    print("w1: ", w1)
    # Getting the values of w2,w3,w4,w5
    t2 = XOR(w0, round_constant_0)
    w2 = XOR(t2, (subNibble(rotateNibble(w1))))
    print("The value of w2 :", w2)
    w3 = XOR(w1, w2)
    print("The value of w3 :", w3)
    t4 = XOR(w2, round_constant_1)
    w4 = XOR(t4, (subNibble(rotateNibble(w3))))
    print("The value of w4 :", w4)
    w5 = XOR(w3, w4)
    print("The value of w5 :", w5)
    return [w0 + w1, w2 + w3, w4 + w5]


input_message = [1, 1, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0]
key = [0, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1]

# Key Generation

keys = keyGeneration(key)
print("The keys generated are :", keys)


# Encryption
round_key = XOR(input_message, keys[0])
for _ in range(0, 2):
    subNibble_round_1 = subNibble(round_key[:8])
    subNibble_round_2 = subNibble(round_key[8:])
    substitution_output = subNibble_round_1 + subNibble_round_2
    print("substitution step output: ", substitution_output)
    shift_rows_output = shiftRows(substitution_output)
    print("The shift rows output :", shift_rows_output)
    if _ == 0:
        mix_columns_output = []
        mix_columns_output = mixColumns(shift_rows_output)
        temp = mix_columns_output[4:8]
        temp2 = mix_columns_output[8:12]

        # Shifting the S01 and S10
        mix_columns_output[4:8] = temp2
        mix_columns_output[8:12] = temp
        print("The result of mix columns :", mix_columns_output)
        round_key = XOR(mix_columns_output, keys[_ + 1])
    else:
        round_key = XOR(shift_rows_output, keys[_ + 1])
print("The cipher text: ", round_key)

# Decryption

# round_key = XOR(round_key, keys[-1])
# keys.pop()

# for _ in range(0, 2):
#     shift_rows_output = shiftRows(substitution_output)
#     print("The shift rows output :", shift_rows_output)
#     if _ == 0:
#         round_key = XOR(shift_rows_output, keys[_ + 1])
#     else:
#         mix_columns_output = []
#         mix_columns_output = mixColumns(shift_rows_output)
#         temp = mix_columns_output[4:8]
#         temp2 = mix_columns_output[8:12]
#
#         # Shifting the S01 and S10
#         mix_columns_output[4:8] = temp2
#         mix_columns_output[8:12] = temp
#         print("The result of mix columns :", mix_columns_output)
#         round_key = XOR(mix_columns_output, keys[_ + 1])
# print("The cipher text: ", round_key)



