def getTheS0S1(list1, list2):
    s0 = [[[0, 1], [0, 0], [1, 1], [1, 0]], [[1, 1], [1, 0], [0, 1], [0, 0]], [[0, 0], [1, 0], [0, 1], [1, 1]],
          [[1, 1], [0, 1], [1, 1], [1, 0]]]
    s1 = [[[0, 0], [0, 1], [1, 0], [1, 1]], [[1, 0], [0, 0], [0, 1], [1, 1]], [[1, 1], [0, 0], [0, 1], [0, 0]],
          [[1, 0], [0, 1], [0, 0], [1, 1]]]
    row1 = int(str(list1[0]) + str(list1[3]), 2)
    column1 = int(str(list1[1]) + str(list1[2]), 2)
    row2 = int(str(list2[0]) + str(list2[3]), 2)
    column2 = int(str(list2[1]) + str(list2[2]), 2)
    return s0[row1][column1] + s1[row2][column2]


def XOR(list1, list2):
    result = []
    for _ in range(len(list1)):
        result.append(list1[_] ^ list2[_])
    return result


def reverseInitialPermutation(input):
    result = []
    rip_code = [4, 1, 3, 5, 7, 2, 8, 6]
    for _ in rip_code:
        result.append(input[_ - 1])
    return result


def initialPermutation(input):
    result = []
    ip_code = [2, 6, 3, 1, 4, 8, 5, 7]
    for _ in ip_code:
        result.append(input[_ - 1])
    return result


def expansion(input):
    expanded_list = []
    expansion_code = [4, 1, 2, 3, 2, 3, 4, 1]
    for _ in expansion_code:
        expanded_list.append(input[_ - 1])
    return expanded_list


def getTheP4(input):
    p4_list = []
    p4_code = [2, 4, 3, 1]
    for _ in p4_code:
        p4_list.append(input[_ - 1])
    return p4_list


def getTheP8(input):
    p8_list = []
    p8_code = [6, 3, 7, 4, 8, 5, 10, 9]
    for _ in p8_code:
        p8_list.append(input[_ - 1])
    return p8_list


def shiftTheList(input):
    temp = list(input[1:])
    temp.append(input[0])
    return temp


def splitTheList(input):
    split_list = []
    split_list.append(list(input[:int(len(input) / 2)]))
    split_list.append(list(input[int(len(input) / 2):]))
    return split_list


def getTheP10(input):
    p10_list = []
    p10_code = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    for _ in p10_code:
        p10_list.append(input[_ - 1])
    return p10_list


plain_text = [1, 0, 1, 0, 1, 0, 0, 1]
key = [1, 0, 0, 0, 1, 0, 0, 0, 1, 1]
keys = []

# key Generation
p10 = getTheP10(key)
left_part, right_part = splitTheList(p10)
for _ in range(0, 2):
    if _ == 0:
        left_shift_1 = shiftTheList(left_part)
        left_shift_2 = shiftTheList(right_part)
    else:
        for __ in range(0, 2):
            left_shift_1 = shiftTheList(left_shift_1)
            left_shift_2 = shiftTheList(left_shift_2)
    combined_list = left_shift_1 + left_shift_2
    keys.append(getTheP8(combined_list))

print("The keys generated are :", keys)

# Encryption/ Decryption
for count in range(0, 2):
    if count == 0:
        permutated_list = initialPermutation(plain_text)
    else:
        permutated_list = initialPermutation(cipher_text)
    left_part, right_part = splitTheList(permutated_list)
    for _ in range(0, 2):
        expanded_list = expansion(right_part)
        if count == 0:
            XORed_list = XOR(expanded_list, keys[_])
        else:
            XORed_list = XOR(expanded_list, keys[-1])
            keys.pop()
        sublist1, sublist2 = splitTheList(XORed_list)
        list_after_S0S1 = getTheS0S1(sublist1, sublist2)
        p4 = getTheP4(list_after_S0S1)
        XORed_list = XOR(left_part, p4)
        if _ == 0:
            left_part = right_part
            right_part = XORed_list
        else:
            cipher_text = reverseInitialPermutation(XORed_list + right_part)
            if count == 0:
                print("The cipher text :", cipher_text)
            else:
                print("The original plain text :", cipher_text)