list = {}
list["apple"] = 3
list["grapes"] = []
list["grapes"].append(1)
bruh = []
bruh.append([3,4])
bruh.append([5,6])
bruh.append(2)
print(list)
print("Bruh",bruh)

listoflist = [[1, 2], [1.3], [1, 5, 6]]
for _ in range(len(listoflist)):
    print(listoflist[_][-1])

dict2 = {"b": [6, 7]}
dict = {"a": [[1, 2], [4, 5]]}
for key, items in dict.items():
    for _ in items:
        print(_)

print(dict["a"][1][0])
print(dict2["b"][1])


