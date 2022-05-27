def readFile(path):
    file = open(path, "r")
    list = file.read().splitlines()
    file.close()
    return list


def writeFile(path, data):
    file = open(path, "w")
    file.writelines(data)
    file.close()


def findNewList(listOne, listTwo):
    return [str + "\n" for str in listOne if str not in listTwo]


listOne = readFile("./input/1.txt")
listTwo = readFile("./input/2.txt")
listOne.sort()
listTwo.sort()
writeFile("./output/1.txt", findNewList(listOne, listTwo))
writeFile("./output/2.txt", findNewList(listTwo, listOne))


# writeFile("./input/1.txt", [str + "\n" for str in listOne])
# writeFile("./input/2.txt", [str + "\n" for str in listTwo])
