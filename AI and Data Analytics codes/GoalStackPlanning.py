predicates = ["on", "ontable", "holding", "armempty", "clear"]
actions = ["putdown", "pickup", "stack", "unstack"]


class Block:
    letter = None
    on = None
    holding = False
    ontable = True
    clear = True

    def __init__(self, letter):
        self.letter = letter


def main():
    number_of_blocks = 4
    initial_state = "(on b a)^(ontable a)^(ontable c)^(ontable d)^(armempty)"
    print("The initial state :" + initial_state)
    initial_state = initial_state.split("^")
    goal_state = "(on d b)^(on c a)^(ontable a)^(ontable d)"
    print("The goal state :" + goal_state)
    goal_state = goal_state.split("^")
    armempty = True
    path = []
    blocks = []
    stack = []

    for i in range(number_of_blocks):
        # Creating an array/ list of objects having letters as follows: a, b, c.
        # Each corresponding to blocks[0],blocks[1],blocks[2]
        # Here The entire object is surrounded by [] because we have to make the blocks[] iterable
        blocks += [Block(letter=(chr(i + 97)))]

    for each in initial_state:
        each = each[1:-1]
        each = each.split(" ")
        if each[0] == "on":
            blocks[ord(each[1]) - 97].on = each[2]  # Gives blocks[ord(a)-97] => blocks[0]
            blocks[ord(each[1]) - 97].clear = True  # doubt here bruh
            blocks[ord(each[2]) - 97].clear = False
            blocks[ord(each[1]) - 97].ontable = False

        elif each[0] == "ontable":
            blocks[ord(each[1]) - 97].holding = False
            blocks[ord(each[1]) - 97].ontable = True

        elif each[0] == "holding":
            blocks[ord(each[1]) - 97].holding = True
            blocks[ord(each[1]) - 97].clear = False
            blocks[ord(each[1]) - 97].ontable = False

        elif each[0] == "clear":
            blocks[ord(each[1]) - 97].clear = True
            blocks[ord(each[1]) - 97].holding = False

    for each in goal_state:
        stack.append(each[1:-1])

    while len(stack) > 0:
        unsplitted_condition = stack.pop()
        print(unsplitted_condition)
        condition = unsplitted_condition.split(" ")

        if condition[0] == "on":
            if blocks[ord(condition[1]) - 97].on != condition[2]:
                stack.append("stack " + condition[1] + " " + condition[2])
                stack.append("holding " + condition[1])
                stack.append("clear " + condition[2])

        elif condition[0] == "holding":
            if not blocks[ord(condition[1]) - 97].holding:
                stack.append("pickup " + condition[1])
                stack.append("clear " + condition[1])
                stack.append("armempty")

        elif condition[0] == "clear":
            if not blocks[ord(condition[1]) - 97].clear:

                for _ in blocks:
                    if _.on == condition[1]:
                        topmost = _.letter
                        break

                stack.append("unstack " + topmost + " " + condition[1])
                stack.append("on " + topmost + " " + condition[1])
                stack.append("clear " + topmost)
                stack.append("armempty")

        elif condition[0] == "ontable":
            if not blocks[ord(condition[1]) - 97].ontable:
                stack.append("putdown " + condition[1])
                stack.append("holding " + condition[1])

        elif condition[0] == "armempty":
            if armempty is False:
                for _ in blocks:
                    if _.holding is True:
                        stack.append("putdown " + _.letter)
                        stack.append("holding " + _.letter)
                        break

        # actions
        elif condition[0] == "stack":
            blocks[ord(condition[1]) - 97].ontable = False
            blocks[ord(condition[1]) - 97].holding = False
            blocks[ord(condition[1]) - 97].clear = True
            blocks[ord(condition[1]) - 97].on = condition[2]
            blocks[ord(condition[2]) - 97].clear = False
            path.append(unsplitted_condition)

        elif condition[0] == "unstack":
            blocks[ord(condition[1]) - 97].ontable = False
            blocks[ord(condition[1]) - 97].holding = True
            blocks[ord(condition[1]) - 97].clear = False
            blocks[ord(condition[1]) - 97].on = None
            blocks[ord(condition[2]) - 97].clear = True
            path.append(unsplitted_condition)
            armempty = False

        elif condition[0] == "pickup":
            blocks[ord(condition[1]) - 97].ontable = False
            blocks[ord(condition[1]) - 97].holding = True
            blocks[ord(condition[1]) - 97].clear = False
            if blocks[ord(condition[1]) - 97].on is not None:
                blocks[ord(blocks[ord(condition[1]) - 97].on) - 97].clear = True
            blocks[ord(condition[1]) - 97].on = None
            path.append(unsplitted_condition)
            armempty = False

        elif condition[0] == "putdown":
            blocks[ord(condition[1]) - 97].ontable = True
            blocks[ord(condition[1]) - 97].holding = False
            blocks[ord(condition[1]) - 97].clear = True
            blocks[ord(condition[1]) - 97].on = None
            path.append(unsplitted_condition)
            armempty = True

    for p in path:
        print("(" + p + ")" + "^", end="")


if __name__ == '__main__':
    main()
