predicates = ["on", "ontable", "holding", "armempty", "clear"]
actions = ["stack", "unstack", "pickup", "putdown"]

'''precondition = {
    'stack a b':[['clear b'],['holding a']],
    'unstack a b': clear a, armempty, on a b
}'''


class Block:
    letter = None
    on = None
    ontable = True
    holding = False
    clear = True

    def __init__(self, letter):
        self.letter = letter


def main():
    number_of_blocks = 3
    blocks = []
    stack = []
    initial_state = "(on a c)^(ontable b)^(ontable c)^(armempty)"
    print("Initial State:" + initial_state)
    initial_state = initial_state.split("^")
    print("After splitting the intital state :",initial_state)
    current_state = initial_state
    ARMEMPTY = True

    path = []

    goal_state = "(on a b)^(on b c)^(ontable c)"
    print("Goal State: " + goal_state)
    goal_state = goal_state.split("^")

    for i in range(int(number_of_blocks)):
        blocks += [Block(letter=(chr(i + 97)))]

    for each in initial_state:
        # removes the brackets  ( = 1 and ) = -1
        each = each[1:-1]
        each = each.split(" ")

        if each[0] == "on":
            # ord() gives the integer value of the character and chr() converts the ascii value to the corresponding character
            blocks[ord(each[1]) - 97].on = each[2]
            blocks[ord(each[1]) - 97].ontable = False
            blocks[ord(each[2]) - 97].clear = False
            blocks[ord(each[1]) - 97].clear = True

        elif each[0] == "ontable":
            blocks[ord(each[1]) - 97].ontable = True
            blocks[ord(each[1]) - 97].holding = False

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
        condition = unsplitted_condition.split(" ")

        #PRECONDITIONS
        if condition[0] == "on":
            if blocks[ord(condition[1]) - 97].on != condition[2]:
                # stack.append(condition)
                # Append action to path and its precondition to stack
                stack.append("stack " + condition[1] + " " + condition[2])
                stack.append("holding " + condition[1])
                stack.append("clear " + condition[2])

        elif condition[0] == "ontable":
            if not blocks[ord(condition[1]) - 97].ontable:
                # putdown
                stack.append("putdown " + condition[1])
                stack.append("holding " + condition[1])

        elif condition[0] == "holding":
            if not blocks[ord(condition[1]) - 97].holding:
                # unstack or pickup
                stack.append("pickup " + condition[1])
                stack.append("clear " + condition[1])
                stack.append("armempty")

        elif condition[0] == "clear":
            if not blocks[ord(condition[1]) - 97].clear:

                for _ in blocks:
                    if _.on == condition[1]:
                        top_element = _.letter

                stack.append("unstack " + top_element + " " + condition[1])
                stack.append("on " + top_element + " " + condition[1])
                stack.append("clear " + top_element)
                stack.append("armempty")

        elif condition[0] == "armempty":
            if ARMEMPTY is False:
                for each in blocks:
                    if each.holding is True:
                        stack.append("putdown " + each.letter)
                        stack.append("holding " + each.letter)
                        break

        # ACTIONS
        elif condition[0] == "stack":
            path.append(unsplitted_condition)
            blocks[ord(condition[1]) - 97].on = condition[2]
            blocks[ord(condition[1]) -97].ontable = False
            blocks[ord(condition[1]) -97].holding = False
            blocks[ord(condition[2]) - 97].clear = False
            blocks[ord(condition[1]) - 97].clear = True

        elif condition[0] == "unstack":
            path.append(unsplitted_condition)
            ARMEMPTY = False
            blocks[ord(condition[2]) - 97].clear = True
            blocks[ord(condition[2]) - 97].holding = False
            blocks[ord(condition[1]) - 97].holding = True
            blocks[ord(condition[1]) - 97].clear = False
            blocks[ord(condition[1]) - 97].on = None
            blocks[ord(condition[1]) - 97].ontable = False

        elif condition[0] == "pickup":
            path.append(unsplitted_condition)
            ARMEMPTY = False
            blocks[ord(condition[1]) - 97].holding = True
            blocks[ord(condition[1]) - 97].ontable = False
            if blocks[ord(condition[1]) - 97].on is not None:
                blocks[ord(blocks[ord(condition[1]) - 97].on) - 97].clear = True
            blocks[ord(condition[1]) - 97].on = None
            blocks[ord(condition[1]) - 97].clear = False

        elif condition[0] == "putdown":
            path.append(unsplitted_condition)
            ARMEMPTY = True
            blocks[ord(condition[1]) - 97].ontable = True
            blocks[ord(condition[1]) - 97].holding = False
            blocks[ord(condition[1]) - 97].on = None
            blocks[ord(condition[1]) - 97].clear = True

    for _ in path:
        print("(" + _ + ") ^ ", end="")


if __name__ == "__main__":
    main()
