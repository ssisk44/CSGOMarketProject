def formatArrayOutput(databaseTupleArray):
    returnArr = []
    for tuple in databaseTupleArray:
        arr = []
        for entry in tuple:
            arr.append(entry)
        returnArr.append(arr)
    return returnArr

def filterIndividualWeaponOutputs(inputArr):
    unique = []
    def checkIsUnique(newEntry):
        for entry in unique:
            if entry[2:4] == newEntry[2:4]:
                return False
        return True
    for entry in inputArr:
        if checkIsUnique(entry):
            unique.append(entry)
    return unique

