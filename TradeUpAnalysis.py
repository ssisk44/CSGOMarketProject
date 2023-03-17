import os
import time
import numpy as np
import pandas as pd
import sys
from selenium import webdriver
import requests
import Tools.WeaponFloatHandler as WFH

rarityHierarchyMap = {
    "Mil_Spec Grade": 0,
    "Restricted": 1,
    "Classified": 2,
    "Covert": 3
}
reverseRarityHierarchyMap = {
    0: "Mil_Spec Grade",
    1: "Restricted",
    2: "Classified",
    3: "Covert"
}
weaponWearArray = [
    'Battle-Scarred',
    'Well-Worn',
    'Field-Tested',
    'Minimal Wear',
    'Factory New'
]


def getAllItemsForACase(caseName):
    allItems = pd.read_csv('Data/Weapons/weapons.csv').to_numpy()
    caseItems = []
    for entry in allItems:
        if entry[2] == caseName:
            caseItems.append(entry)
    return caseItems


def distributeCaseItemsByRarityName(caseName, stattrak=0):
    caseItems = getAllItemsForACase(caseName)
    milSpec = []
    restricted = []
    classified = []
    covert = []
    for entry in caseItems:
        if entry[4] == 'Mil_Spec Grade' and entry[5] == stattrak:
            milSpec.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-7], 2)])
        elif entry[4] == 'Restricted' and entry[5] == stattrak:
            restricted.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-7], 2)])
        elif entry[4] == 'Classified' and entry[5] == stattrak:
            classified.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-7], 2)])
        elif entry[4] == 'Covert' and entry[5] == stattrak:
            covert.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-7], 2)])
    return [milSpec, restricted, classified, covert]


def getUniqueGunSkinsFromRarityLevel(thisRarityLevel):
    uniqueEntries = []
    returnArr = []
    for entry in thisRarityLevel:
        newEntry = [entry[0], entry[1]]
        if newEntry not in uniqueEntries:
            uniqueEntries.append(newEntry)
            returnArr.append(newEntry + [entry[-1]])
    return returnArr


def filterArray(array, index, value):
    filteredArray = []
    for entry in array:
        if entry[index] == value:
            filteredArray.append(entry)
    return filteredArray


def newAnalysisFunction(caseName):
    caseItemsByRarityNonStatTrak = distributeCaseItemsByRarityName(caseName)
    # caseItemsByRarityStatTrak = distributeCaseItemsByRarityName(caseName, 1)

    # for each rarity level in a case
    for rarityLevel in caseItemsByRarityNonStatTrak:
        print("BEGINNING RARITY LEVEL:", rarityLevel[0][4])
        thisRarityLevelName = rarityLevel[0][4]
        # get all items from the next tier of rarity array
        nextRarityLevelArr = caseItemsByRarityNonStatTrak[rarityHierarchyMap[thisRarityLevelName] + 1]

        # filter for each individual gun of next rarity level
        thisRaritiesGuns = getUniqueGunSkinsFromRarityLevel(rarityLevel)
        nextRaritiesGuns = getUniqueGunSkinsFromRarityLevel(nextRarityLevelArr)
        for item in thisRaritiesGuns:
            print("Starting analysis of weapon: ", item[0], item[1])
            if thisRarityLevelName in ["Mil_Spec Grade", "Restricted", "Classified"]:
                floatNum = 0.0000005 #offset insures it falls into ranges definined in weapons float handler wear range
                itemEntries = []
                while floatNum < 1.000:
                    thisFloatEntryArray = []
                    thisFloatEntryArray.append(round((floatNum), 2))  # float num
                    thisFloatEntryArray.append(item[0])  # weapon name
                    thisFloatEntryArray.append(item[1])  # skin name
                    thisPrice = WFH.getTradeUpFloat(item[0], item[1], floatNum)[2]
                    thisFloatEntryArray.append(thisPrice)  # individual weapon cost
                    tradeUpCost = round(thisPrice * 10, 2)
                    thisFloatEntryArray.append(tradeUpCost)  # full trade up cost

                    # for each next rarity append the average price of the converted float weapon
                    priceAvg = 0.00
                    for nRG in nextRaritiesGuns:
                        gunTradeUpFloat = WFH.getTradeUpFloat(nRG[0], nRG[1], floatNum)
                        ### DEBUG
                        # gun = nRG[0]
                        # skin = nRG[1]
                        # adjustedFloat = round(gunTradeUpFloat[0], 6)
                        # wear = gunTradeUpFloat[1]
                        price = gunTradeUpFloat[2]
                        # thisFloatEntryArray.append([gun] + [skin] + [adjustedFloat] + [wear] + [price])
                        priceAvg += price
                    tradeUpProfit = round(priceAvg/len(nextRaritiesGuns), 2)
                    thisFloatEntryArray.append(tradeUpProfit)

                    netProfit = round(tradeUpProfit - tradeUpCost, 2)
                    thisFloatEntryArray.append(netProfit)

                    profitAfterSteam = round(netProfit * (7 / 8), 2)
                    thisFloatEntryArray.append(profitAfterSteam)

                    roi = round(profitAfterSteam / tradeUpCost * 100, 2)
                    thisFloatEntryArray.append(roi)

                    itemEntries.append(thisFloatEntryArray)

                    floatNum = round(floatNum + .001, 10)

                # write each case/grade/gun&skin to csv
                weaponNameAndSkin = str(item[0]) + ' ' + str(item[1])
                df = pd.DataFrame(data=np.array(itemEntries), columns=['Float', 'Weapon Name', 'Skin Name', 'Single Cost ($)', '10x Cost ($)', 'Average Profit ($)', 'Net Profit ($)', 'Net Profit After Steam ($)', 'ROI %'])
                df.to_csv('Analysis/FloatTables/'+caseName.replace(' ', '_')+'/'+thisRarityLevelName.replace(' ', '_')+'/'+weaponNameAndSkin.replace(' ', '_')+'.csv', index=False)



newAnalysisFunction('Chroma 2 Case')
