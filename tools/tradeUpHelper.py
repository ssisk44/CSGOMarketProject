import controllers.wearController as wC
import controllers.weaponSkinController as wSC

reverseWearMap = wC.reverseWearMap

def getCheapestTradeUpChoice(entries):
    cheapestPrice = 999999
    cheapestEntry = None
    for entry in entries:
        price = entry[-1]
        # and weapon completely within float range (exclude range cut off weapons only in their cut off wear ranges)
        if price > 0 and price < cheapestPrice:
            cheapestPrice = price
            cheapestEntry = entry
    if cheapestEntry is None:
        return False
    return cheapestEntry

def getNextRarityLevelAveragePrice(containerSkins, rarity_int:int, outputWear:str, isCollection, isStatOrSouv, debug = False):
    """
    TESTED AND WORKING
    :param containerEntries:
    :param rarity_int:
    :param outputWear:
    :param isCollection:
    :param isStatOrSouv:
    :return:
    """
    r_int = rarity_int + 1
    isColl = 0
    if isCollection:
        isColl = 1
    entries = wSC.getEntries(containerSkins, r_int, outputWear, isColl, isStatOrSouv)
    if debug:
        print(entries)
    totalPrice = 0
    numWeapons = 0
    for entry in entries:
        price = entry[-1]
        if type(price) == float and price > 0:
            numWeapons += 1
            totalPrice += price

    average = round(totalPrice/numWeapons, 2)
    return average

def getCombinationInputsPrice(map, combination, rarityLevelName, debug = False):
    """TESTED AND WORKING"""
    # iterate through combination to calculate inputs price
    combinationArr = combination[2]
    totalPrice = 0
    for index in range(0, len(combinationArr)):
        if combinationArr[index] > 0:
            wearLevelName = reverseWearMap[index]
            numberValue = combinationArr[index]
            price = map[rarityLevelName][wearLevelName][-1]
            if debug:
                print(combinationArr, numberValue, rarityLevelName, wearLevelName, map[rarityLevelName][wearLevelName], map[rarityLevelName][wearLevelName][-1])
            priceMultiplierTotal = numberValue * price
            totalPrice += priceMultiplierTotal
    returnPrice = round(totalPrice, 2)
    return returnPrice
