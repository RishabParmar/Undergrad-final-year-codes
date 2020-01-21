predicates = ["holding", "armempty", "ontable", "on", "clear"]
actions = ["stack", "unstack", "pickup", "putdown"]

class Block:
    letter = None
    holding = False
    ontable = True
    clear = True
    on = None

    def __init__(self, letter):
        self.letter = letter


def main():
    noblocks = 3
    initial_state = "(on a c)^(ontable b)^(ontable c)^(armempty)"
    initial_state = initial_state.split("^")
    goal_state = "(on a b)^(on b c)^(ontable c)"
    goal_state = goal_state.split("^")
    armempty = True
    path = []
    stack = []
    block = []
    for i in range(noblocks):
        block += [Block(letter=chr(i+97))]

    for each in initial_state:
        each = each[1:-1]
        each = each.split(" ")
        if each[0] == "on":
            block[ord(each[1])-97].on = each[2]
            block[ord(each[1])-97].clear = True
            block[ord(each[2])-97].clear = False
            block[ord(each[1])-97].ontable = False
        elif each[0] == "ontable":
            block[ord(each[1]) - 97].ontable = True
            block[ord(each[1]) - 97].holding = False
            print()
        elif each[0] == "clear":
            block[ord(each[1]) - 97].clear = True
            block[ord(each[1]) - 97].holding = False
        elif each[0] == "holding":
            block[ord(each[1]) - 97].clear = False
            block[ord(each[1]) - 97].holding = True
            block[ord(each[1]) - 97].ontable = False

    for each in goal_state:
        stack.append(each[1:-1])

    while len(stack) > 0:
        unsplitted_condition = stack.pop()
        print(unsplitted_condition)
        condition = unsplitted_condition.split(" ")

        if condition[0] == "ontable":
            if not block[ord(condition[1])-97].ontable:
                stack.append("putdown "+condition[1])
                stack.append("holding "+condition[1])

        elif condition[0] == "on":
            if block[ord(condition[1])-97].on != condition[2]:
                stack.append("stack " + condition[1]+" "+condition[2])
                stack.append("holding " + condition[1])  #
                stack.append("clear " + condition[2])

        elif condition[0] == "holding":
            if not block[ord(condition[1])-97].holding:
                stack.append("pickup " + condition[1])
                stack.append("clear " + condition[1])
                stack.append("armempty")

        elif condition[0] == "clear":
            if not block[ord(condition[1]) - 97].clear:
                for _ in block:
                    if _.on == condition[1]:
                        topmost = _.letter
                        break
                stack.append("unstack " + topmost + " " + condition[1])
                stack.append("on " + topmost + " " + condition[1])
                stack.append("clear " + topmost)
                stack.append("armempty")

        elif condition[0] == "armempty":
            if armempty is False:
                for _ in block:
                    if _.holding is True:
                        stack.append("putdown " + _.letter)
                        stack.append("holding " + _.letter)
                        break

        elif condition[0] == "stack":
            path.append(unsplitted_condition)
            block[ord(condition[1])-97].on = condition[2]
            block[ord(condition[1]) - 97].clear = True
            block[ord(condition[1]) - 97].ontable = False
            block[ord(condition[2]) - 97].clear = False
            block[ord(condition[1]) - 97].holding = False
            armempty = True

        elif condition[0] == "unstack":
            path.append(unsplitted_condition)
            block[ord(condition[1]) - 97].on = None
            block[ord(condition[1]) - 97].clear = False
            block[ord(condition[2]) - 97].clear = True
            block[ord(condition[1]) - 97].holding = True
            armempty = False

        elif condition[0] == "pickup":
            path.append(unsplitted_condition)
            block[ord(condition[1]) - 97].clear = False
            block[ord(condition[1]) - 97].ontable = False
            block[ord(condition[1]) - 97].on = None
            if block[ord(condition[1])-97].on is not None:
                block[ord(block[ord(condition[1])-97].on)-97].clear = True
            block[ord(condition[1]) - 97].holding = True
            armempty = False

        elif condition[0] == "putdown":
            path.append(unsplitted_condition)
            block[ord(condition[1]) - 97].ontable = True
            block[ord(condition[1]) - 97].clear = True
            block[ord(condition[1]) - 97].holding = False
            block[ord(condition[1]) - 97].on = None  #
            armempty = True

    print("The path is as follows: ")
    for i in path:
        print("("+i+")", end="")


if __name__ == '__main__':
    main()