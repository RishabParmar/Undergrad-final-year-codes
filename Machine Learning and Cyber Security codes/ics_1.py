def inverseInitialPermutation(input):
    rip_code = [4, 1, 3, 5, 7, 2, 8, 6]
    r_list = []
    for _ in rip_code:
        r_list.append(input[_ - 1])
    return r_list


def getTheP4(k):
    p4_code = [2, 4, 3, 1]
    p4_list = []
    for _ in p4_code:
        p4_list.append(k[_ - 1])
    return p4_list


def getTheS0S1Permutations(list1, list2):
    s0 = [[[0, 1], [0, 0], [1, 1], [1, 0]], [[1, 1], [1, 0], [0, 1], [0, 0]], [[0, 0], [1, 0], [0, 1], [1, 1]],
          [[1, 1], [0, 1], [1, 1], [1, 0]]]
    s1 = [[[0, 0], [0, 1], [1, 0], [1, 1]], [[1, 0], [0, 0], [0, 1], [1, 1]], [[1, 1], [0, 0], [0, 1], [0, 0]],
          [[1, 0], [0, 1], [0, 0], [1, 1]]]
    row1 = int(str(list1[0]) + str(list1[3]), 2)
    column1 = int(str(list1[1]) + str(list1[2]), 2)
    row2 = int(str(list2[0]) + str(list2[3]), 2)
    column2 = int(str(list2[1]) + str(list2[2]), 2)
    return s0[row1][column1] + s1[row2][column2]


def getTheExpansion(message):
    expansion_code = [4, 1, 2, 3, 2, 3, 4, 1]
    temp = []
    for _ in expansion_code:
        temp.append(message[_ - 1])
    return temp


def XOR(list1, list2):
    result = []
    for _ in range(len(list1)):
        result.append(list1[_] ^ list2[_])
    return result


def getTheinitialPermutation(message):
    ip_code = [2, 6, 3, 1, 4, 8, 5, 7]
    temp = []
    for _ in ip_code:
        temp.append(message[_ - 1])
    return temp


def getTheP8(k):
    p8_code = [6, 3, 7, 4, 8, 5, 10, 9]
    p8_list = []
    for _ in p8_code:
        p8_list.append(k[_ - 1])
    return p8_list


def shiftingTheList(k):
    temp = list(k[1:])
    temp.append(k[0])
    return temp


def splitTheList(k):
    split_lists = []
    split_len = int(len(k) / 2)
    split_lists.append(list(k[:split_len]))
    split_lists.append(list(k[split_len:]))
    return split_lists


def getTheP10(k):
    p10_code = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p10_list = []
    for _ in p10_code:
        p10_list.append(k[_ - 1])
    return p10_list


input_message = [1, 0, 1, 0, 1, 0, 0, 1]
key = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
keys = []

# Key generation

p10 = getTheP10(key)
left_half, right_half = splitTheList(p10)
for _ in range(0, 2):
    if _ == 0:
        left_shift_1 = shiftingTheList(left_half)
        left_shift_2 = shiftingTheList(right_half)
    else:
        for i in range(0, 2):
            left_shift_1 = shiftingTheList(left_shift_1)
            left_shift_2 = shiftingTheList(left_shift_2)
    combined_list = left_shift_1 + left_shift_2
    keys.append(getTheP8(combined_list))

print("Keys :", keys)

# Encryption/ Decryption
for count in range(0, 2):
    if count == 0:
        permutated_message = getTheinitialPermutation(input_message)
    else:
        permutated_message = getTheinitialPermutation(cipher_text)
    left_part, right_part = splitTheList(permutated_message)
    for _ in range(0, 2):
        expanded_list = getTheExpansion(right_part)
        if count == 0:
            XORed_list = XOR(expanded_list, keys[_])
        else:
            XORed_list = XOR(expanded_list, keys[-1])
            keys.pop()
        sublist_1, sublist_2 = splitTheList(XORed_list)
        list_after_S0_S1 = getTheS0S1Permutations(sublist_1, sublist_2)
        p4 = getTheP4(list_after_S0_S1)
        XORed_list = XOR(p4, left_part)
        if _ == 0:
            left_part = right_part
            right_part = XORed_list
        else:
            cipher_text = inverseInitialPermutation(XORed_list + right_part)
            if count == 0:
                print("The cipher text :", cipher_text)
            else:
                print("The original plain text :", cipher_text)
