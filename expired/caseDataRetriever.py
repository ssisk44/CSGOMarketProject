
def mergeAllCasesIntoOne():
    # should never be needed to be used again as cases are static
    allCases = []
    for file in os.listdir('tmp/Cases/'):
        if file != 'ALL_CASES.csv':
            caseArr = pd.read_csv('tmp/Cases/' + file).to_numpy().tolist()
            for item in caseArr:
                allCases.append(item)
    df = pd.DataFrame(data=allCases, columns=['Name', 'Case', 'Skin', 'Rarity'])
    df.to_csv('tmp/Cases/ALL_CASES.csv', index=False)

def getCaseAndRarityOfItem(weaponName, skinName):
    allCasesWeaponsArr = pd.read_csv('tmp/Cases/ALL_CASES.csv').to_numpy()
    for entry in allCasesWeaponsArr:
        if entry[0] == weaponName and entry[2] == skinName:
            return [entry[1], entry[3]]
    return None

def addCaseAndWearToAllItems():
    # this function finds all CASE ITEMS (not collections) from weaponsMiscellaneous.csv and adds columns for the wear and case, and creates agents csv
    allWeaponsArr = pd.read_csv('tmp/Weapons/weaponsMiscellaneous.csv').to_numpy()
    agentsArr = []
    newWeaponsArray = []
    caseItemsFoundCounter = 0
    for entry in allWeaponsArr:
        fullNameAndWear = entry[2]
        fullNameAndWear = fullNameAndWear.replace(' (', ' | ')
        fullNameAndWear = fullNameAndWear.replace(')', '')
        splitArr = fullNameAndWear.split(' | ')

        if len(splitArr) == 2:
            # music kits, agents, patch, graffiti all found here
            agentsArr.append(entry)

        elif len(splitArr) == 3:
            weaponName = splitArr[0]
            skinName = splitArr[1]
            wearName = splitArr[2]
            statTrakBoolean = 0

            # parse stattrak info
            if 'StatTrak' in weaponName:
                statTrakBoolean = 1
                weaponName = weaponName.split('™ ')[1]

            caseRes = getCaseAndRarityOfItem(weaponName, skinName)
            if caseRes is None:
                continue  # collection fall through here

            caseItemsFoundCounter += 1
            caseName = caseRes[0]
            rarityName = caseRes[1]
            newEntry = [weaponName, skinName, caseName, wearName, rarityName, statTrakBoolean]
            thisEntryList = entry.tolist()
            for i in thisEntryList:
                newEntry.append(i)
            newWeaponsArray.append(newEntry)

    weaponsCols = ['weaponName', 'skinName', 'caseName', 'wearName', 'rarityName', 'StatTrak']
    for i in columnNames:
        weaponsCols.append(i)

    # write weapons array
    df = pd.DataFrame(data=np.array(newWeaponsArray), columns=weaponsCols)
    df.to_csv('tmp/Weapons/weapons.csv', index=False)

    # write agents array
    df = pd.DataFrame(data=np.array(agentsArr), columns=columnNames)
    df.to_csv('tmp/Agents/agents.csv', index=False)

    print("Total case items: 646 * 5 (wear per item) * 2 (statrak and normal variant = 6460")
    print("Total items found that matched case items:", caseItemsFoundCounter)
