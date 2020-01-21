def reverseInitialPermutation(input):
    rip_code = [4, 1, 3, 5, 7, 2, 8, 6]
    r_list = []
    for _ in rip_code:
        r_list.append(input[_ - 1])
    return r_list


def getTheP4(input):
    p4_code = [2, 4, 3, 1]
    p4_list = []
    for _ in p4_code:
        p4_list.append(input[_ - 1])
    print("The p8_list is :", p4_list)
    return p4_list


def getTheS0S1PermutatedList(list1, list2):
    s0 = [[[0, 1], [0, 0], [1, 1], [1, 0]], [[1, 1], [1, 0], [0, 1], [0, 0]], [[0, 0], [1, 0], [0, 1], [1, 1]],
          [[1, 1], [0, 1], [1, 1], [1, 0]]]
    s1 = [[[0, 0], [0, 1], [1, 0], [1, 1]], [[1, 0], [0, 0], [0, 1], [1, 1]], [[1, 1], [0, 0], [0, 1], [0, 0]],
          [[1, 0], [0, 1], [0, 0], [1, 1]]]
    row1 = int(str(list1[0]) + str(list1[3]), 2)
    column1 = int(str(list1[1]) + str(list1[2]), 2)
    row2 = int(str(list2[0]) + str(list2[3]), 2)
    column2 = int(str(list2[1]) + str(list2[2]), 2)
    temp = s0[row1][column1] + s1[row2][column2]
    print("The list after s0 s1 :", temp)
    return temp


def XOR(list1, list2):
    result = []
    for _ in range(len(list1)):
        result.append(list1[_] ^ list2[_])
    return result


def expansionPermutation(input):
    temp = []
    expansion_code = [4, 1, 2, 3, 2, 3, 4, 1]
    for _ in expansion_code:
        temp.append(input[_ - 1])
    print("The expanded list :", temp)
    return temp


def initialPermutation(input):
    ip_code = [2, 6, 3, 1, 4, 8, 5, 7]
    temp = []
    for _ in ip_code:
        temp.append(input[_ - 1])
    print("The initial permutation list :", temp)
    return temp


def getTheP8(input):
    p8_code = [6, 3, 7, 4, 8, 5, 10, 9]
    p8_list = []
    for _ in p8_code:
        p8_list.append(input[_ - 1])
    print("The p8_list is :", p8_list)
    return p8_list


def shifftingTheList(input):
    temp = list(input[1:])
    temp.append(input[0])
    return temp


def splitTheList(input):
    split_input = []
    split_len = int(len(input) / 2)
    split_input.append(list(input[:split_len]))
    split_input.append(list(input[split_len:]))
    return split_input


def getTheP10(k):
    p10_code = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
    p10_list = []
    for _ in p10_code:
        p10_list.append(k[_ - 1])
    print("The p10_list is :", p10_list)
    return p10_list


# --------------------------------- Taking the input from the user (Key and input message)
input_message = [1, 0, 1, 0, 1, 0, 0, 0]
key = [0, 0, 1, 0, 1, 1, 0, 1, 0, 0]
keys = []
print("The input message :", input_message)
print("Key :", key)

# --------------------------------------- Generating the round keys

# Applying P10
p10 = getTheP10(key)
ls_key, rs_key = splitTheList(p10)

for _ in range(0, 2):
    # Split the lists into two halves
    if _ == 0:
        ls_shift_1 = shifftingTheList(ls_key)
        rs_shift_1 = shifftingTheList(rs_key)
    else:
        for k in range(0, 2):
            ls_shift_1 = shifftingTheList(ls_shift_1)
            rs_shift_1 = shifftingTheList(rs_shift_1)
    combined_shift_list = ls_shift_1 + rs_shift_1
    # Applying P8
    p8 = getTheP8(combined_shift_list)
    keys.append(p8)

print("The keys that are generated are as follows: ", keys)

# -------------------------- Encryption
for count in range(0, 2):
    if count == 0:
        permutated_input = initialPermutation(input_message)
    else:
        permutated_input = initialPermutation(cipher_text)
    left_part, right_part = splitTheList(permutated_input)
    for _ in range(0, 2):
        expanded_sub_list = expansionPermutation(right_part)
        if count == 0:
            xored_list = XOR(keys[_], expanded_sub_list)
        else:
            xored_list = XOR(keys[-1], expanded_sub_list)
            keys.pop(-1)
        sub_list_part_1, sub_list_part_2 = splitTheList(xored_list)
        list_after_s0_s1 = getTheS0S1PermutatedList(sub_list_part_1, sub_list_part_2)
        p4_output = getTheP4(list_after_s0_s1)
        xored_list = XOR(p4_output, left_part)
        # End of the iteration
        if _ == 0:
            left_part = right_part
            right_part = xored_list
        else:
            cipher_text = reverseInitialPermutation(xored_list + right_part)
            if count == 0:
                print("The cipher text :", cipher_text)
                print("------------------------------------Encryption over------------------------------------")
            else:
                print("The original plain text :", cipher_text)
