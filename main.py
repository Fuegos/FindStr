def readFile(path):
    file = open(path, "r")
    list = file.read().splitlines()
    file.close()
    return list


def writeFile(path, data):
    file = open(path, "w")
    file.writelines(data)
    file.close()

def prepareForWrite(list):
    return [str + "\n" for str in list]


def findUnique(rangeOne, rangeTwo):
    return [str for str in rangeOne if str not in rangeTwo]


# Create dictonary with first string's symbol and his area
def createMask(file):
    mask = {}
    for index, str in enumerate(file):
        if str[0] in mask:
            mask[str[0]]["end"] = index + 1
        else:
            mask[str[0]] = {"start": index, "end": index + 1}
    return mask


def getRangeByMask(key, file, mask):
    return file[mask[key]["start"]:mask[key]["end"]]


def findList(fileOne, maskOne, fileTwo, maskTwo):
    result = []
    for key in maskOne:
        if key in maskTwo:
            result.extend(
                findUnique(
                    getRangeByMask(key, fileOne, maskOne),
                    getRangeByMask(key, fileTwo, maskTwo)
                )
            )
        else:
            result.extend(
                getRangeByMask(key, fileOne, maskOne)
            )
    return result



fileOne = readFile("./input/1.txt")
fileTwo = readFile("./input/2.txt")

maskOne = createMask(fileOne)
maskTwo = createMask(fileTwo)

listOne = findList(fileOne, maskOne, fileTwo, maskTwo)
listTwo = findList(fileTwo, maskTwo, fileOne, maskOne)


writeFile("./output/1.txt", prepareForWrite(listOne))
writeFile("./output/2.txt", prepareForWrite(listTwo))

# writeFile("./input/1.txt", [str + "\n" for str in listOne])
# writeFile("./input/2.txt", [str + "\n" for str in listTwo])
