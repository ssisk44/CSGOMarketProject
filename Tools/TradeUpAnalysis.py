import os
import time
import numpy as np
import pandas as pd
import sys
from selenium import webdriver
import requests
import Tools.WeaponFloatHandler as WFH
import Tools.PriceHandler as PH
import Tools.FileHandler as FH


# https://csgoskins.gg/markets/market-csgo

def getAllItemsForACase(caseName):
    allItems = pd.read_csv('../Data/Weapons/weapons.csv').to_numpy()
    caseItems = []
    for entry in allItems:
        if entry[2] == caseName:
            caseItems.append(entry)
    return caseItems


def parseDataFromAllCaseItems(allCaseItems):
    retArr = []
    for entry in allCaseItems:
        retArr.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-7], 2)])
    return retArr


def getUniqueItemsFromArray(array, gunName=True, skinName=True, wearName=True, returnUnique=False):
    uniqueEntries = []
    retArr = []
    for entry in array:
        newEntry = []

        # optional selection of unique specifications
        if gunName:
            newEntry.append(entry[0])
        if skinName:
            newEntry.append(entry[1])
        if wearName:
            newEntry.append(entry[3])
        newEntry.append(entry[5])

        if newEntry not in uniqueEntries:
            uniqueEntries.append(newEntry)
            if returnUnique:
                retArr.append(entry[0:2] + entry[4:])
            else:
                retArr.append(entry[0:2] + entry[3:])

    return retArr


# generating all 10 billion skin combinations per float is too expensive, this is my cheap implementation at attempting
# to fully search the profitability of single weapon skin wear mixing profitability :)

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
wearArray = [
    'Factory New',
    'Minimal Wear',
    'Field-Tested',
    'Well-Worn',
    'Battle-Scarred'
]
wearMap = {
    'Factory New': 0,
    'Minimal Wear': 1,
    'Field-Tested': 2,
    'Well-Worn': 3,
    'Battle-Scarred': 4
}
reverseWearMap = {
    0: 'Factory New',
    1: 'Minimal Wear',
    2: 'Field-Tested',
    3: 'Well-Worn',
    4: 'Battle-Scarred'
}
wearRangeMap = {
    'Factory New': [0.00, 0.0699999999999999999999999999999999999],
    'Minimal Wear': [0.07, 0.149999999999999999999999999999999999],
    'Field-Tested': [0.15, 0.379999999999999999999999999999999999],
    'Well-Worn': [0.38, 0.449999999999999999999999999999999999],
    'Battle-Scarred': [0.45, 1.00]
}

FN = [
    [
        [[10, 0, 0, 0, 0], [10, 0, 0, 0, 0]]
    ],
    [
        [[9, 1, 0, 0, 0], [1, 9, 0, 0, 0]]
    ],
    [
        [[8, 1, 1, 0, 0], [1, 1, 8, 0, 0]],
        [[9, 0, 1, 0, 0], [1, 0, 9, 0, 0]],
    ],
    [
        [[7, 1, 1, 1, 0], [1, 1, 1, 7, 0]],
        [[8, 1, 0, 1, 0], [1, 1, 0, 8, 0]],
        [[8, 0, 1, 1, 0], [1, 0, 1, 8, 0]],
        [[9, 0, 0, 1, 0], [1, 0, 0, 9, 0]],
    ],
    [
        [[6, 1, 1, 1, 1], [1, 1, 1, 1, 6]],
        [[7, 1, 1, 0, 1], [1, 1, 1, 0, 7]],
        [[7, 1, 0, 1, 1], [1, 1, 0, 1, 7]],
        [[8, 1, 0, 0, 1], [1, 1, 0, 0, 8]],
        [[7, 0, 1, 1, 1], [1, 0, 1, 1, 7]],
        [[8, 0, 1, 0, 1], [1, 0, 1, 0, 8]],
        [[8, 0, 0, 1, 1], [1, 0, 0, 1, 8]],
        [[9, 0, 0, 0, 1], [1, 0, 0, 0, 9]]
    ]
]

MW = [
    [
        [[], []]
    ],
    [
        [[0, 10, 0, 0, 0], [0, 10, 0, 0, 0]]
    ],
    [
        [[0, 9, 1, 0, 0], [0, 1, 9, 0, 0]]
    ],
    [
        [[0, 8, 1, 1, 0], [0, 1, 1, 8, 0]],
        [[0, 9, 0, 1, 0], [0, 1, 0, 9, 0]]
    ],
    [
        [[0, 7, 1, 1, 1], [0, 1, 1, 1, 7]],
        [[0, 8, 1, 0, 1], [0, 1, 1, 0, 8]],
        [[0, 8, 0, 1, 1], [0, 1, 0, 1, 8]],
        [[0, 9, 0, 0, 1], [0, 1, 0, 0, 9]]
    ]
]

FT = [
    [
        [[], []]
    ],
    [
        [[], []]
    ],
    # field tested only
    [
        [[0, 0, 10, 0, 0], [0, 0, 10, 0, 0]]
    ],
    # field tested and well worn
    [
        [[0, 0, 9, 1, 0], [0, 0, 1, 9, 0]]
    ],
    # field tested, well worn, battle scarred
    [
        [[0, 0, 8, 1, 1], [0, 0, 1, 1, 8]],
        [[0, 0, 9, 0, 1], [0, 0, 1, 0, 9]]
    ]
]

WW = [
    [
        [[], []]
    ],
    [
        [[], []]
    ],
    [
        [[], []]
    ],
    [
        [[0, 0, 0, 10, 0], [0, 0, 0, 10, 0]]
    ],
    [
        [[0, 0, 0, 9, 1], [0, 0, 0, 1, 9]]
    ]
]

BS = [
    [
        [[], []]
    ],
    [
        [[], []]
    ],
    [
        [[], []]
    ],
    [
        [[], []]
    ],
    [
        [[0, 0, 0, 0, 10], [0, 0, 0, 0, 10]]
    ]
]

wearCountSections = [FN, MW, FT, WW, BS]


def theFinalSolution(caseName):
    allCaseItems = getAllItemsForACase(caseName)
    allCaseItemsData = parseDataFromAllCaseItems(allCaseItems)
    allIndividualWeaponsInCase = getUniqueItemsFromArray(allCaseItemsData, gunName=True, skinName=True, wearName=False, returnUnique=True)
    # for each rarity level in a case

    for thisWeapon in allIndividualWeaponsInCase:
        thisWeaponResults = []
        thisWeaponName = thisWeapon[0]
        thisWeaponSkin = thisWeapon[1]
        thisWeaponRarity = thisWeapon[2]
        if thisWeaponRarity in ['Mil_Spec Grade', 'Classified', 'Restricted']:
            thisWeaponRarityInteger = rarityHierarchyMap[thisWeaponRarity]
            tradeUpWeaponRarityInteger = thisWeaponRarityInteger + 1
            tradeUpWeaponRarity = reverseRarityHierarchyMap[tradeUpWeaponRarityInteger]
            thisWeaponIsStatTrak = (thisWeapon[3] == 1)
            thisWeaponStatTrakStr = 'StatTrak'
            if thisWeaponIsStatTrak:
                thisStattrakBool = 1
            else:
                thisWeaponStatTrakStr = ''
                thisStattrakBool = 0

            print("Beginning Weapon", thisWeaponStatTrakStr, thisWeaponName, thisWeaponSkin, thisWeaponRarity)

            # create nextRarity arrays required for trade up valuations
            nextRarityUniqueWeaponSkinWear = []
            nextRarityWeaponsWearPriceMap = {}
            for item in allCaseItemsData:
                if ([item[0], item[1], item[3], item[4], item[5]] not in nextRarityUniqueWeaponSkinWear) and (item[4] == tradeUpWeaponRarity) and item[5] == thisStattrakBool:
                    nextRarityUniqueWeaponSkinWear.append([item[0], item[1], item[3]])
                    if str(item[1]) not in nextRarityWeaponsWearPriceMap:
                        nextRarityWeaponsWearPriceMap[str(item[1])] = {
                            'Factory New': None,
                            'Minimal Wear': None,
                            'Field-Tested': None,
                            'Well-Worn': None,
                            'Battle-Scarred': None
                        }
                    nextRarityWeaponsWearPriceMap[str(item[1])][item[3]] = item[6]
            print(nextRarityWeaponsWearPriceMap)
            nextRarityUniqueWeapons = []
            for weapon in nextRarityUniqueWeaponSkinWear:
                if [weapon[0], weapon[1]] not in nextRarityUniqueWeapons:
                    nextRarityUniqueWeapons.append([weapon[0], weapon[1]])

            # TIME FOR THE HEAVY LIFTING >:D
            # get item float cap
            thisFloatCap = WFH.getFloatCapsByWeaponNameSkinName(thisWeaponName, thisWeaponSkin,
                                                                '../Data/Float/floatCaps.csv')

            thisFloatCapMin = thisFloatCap[0]
            thisFloatCapMax = thisFloatCap[1]
            thisWearRange = ['', '']

            # adjusted for each gun based on float caps for min max to be obtained later
            thisWearRangeMap = {
                'Factory New': [0.00, 0.0699999999999999999999999999999999999],
                'Minimal Wear': [0.07, 0.149999999999999999999999999999999999],
                'Field-Tested': [0.15, 0.379999999999999999999999999999999999],
                'Well-Worn': [0.38, 0.449999999999999999999999999999999999],
                'Battle-Scarred': [0.45, 1.00]
            }

            def makeThisWearRange():
                for wear in wearRangeMap:
                    wearRange = wearRangeMap[wear]
                    wearMin = wearRange[0]
                    wearMax = wearRange[1]
                    if wearMin <= thisFloatCapMin <= wearMax:
                        thisWearRange[0] = wear
                        thisWearRangeMap[wear] = [thisFloatCapMin, thisWearRangeMap[wear][1]]
                    if wearMin < thisFloatCapMax <= wearMax:
                        thisWearRange[1] = wear
                        thisWearRangeMap[wear] = [thisWearRangeMap[wear][0], thisFloatCapMax]

            makeThisWearRange()
            thisWearMin = thisWearRange[0]
            thisWearMax = thisWearRange[1]
            thisWearMinInteger = wearMap[thisWearMin]
            thisWearMaxInteger = wearMap[thisWearMax]

            # create price for wear arr
            thisWeaponPriceArr = [None, None, None, None, None]
            wearCount = thisWearMinInteger
            while wearCount <= thisWearMaxInteger:
                thisWearPrice = PH.getWeaponPrice(thisWeaponName, thisWeaponSkin, reverseWearMap[wearCount], thisStattrakBool)
                thisWeaponPriceArr[wearCount] = thisWearPrice
                wearCount += 1

            # wearMin/Max integers serve as the array range and indexes for values price value combinations
            # get this weapons wear combinations
            thisWearCountEntries = []
            for section in wearCountSections[thisWearMinInteger: thisWearMaxInteger + 1]:
                for thisSectionWearCombinations in section[thisWearMinInteger: thisWearMaxInteger + 1]:
                    thisWearCountEntries.append(thisSectionWearCombinations[0])
            #debug
            # print(thisWeaponPriceArr)
            def getAverageFloat(arr, rangeDelimiter):
                if rangeDelimiter == 'Max':
                    rangeInteger = 0
                else:
                    rangeInteger = 1

                finalFloat = 0.00
                indexCount = 0
                for number in arr:
                    if number > 0:
                        finalFloat += thisWearRangeMap[reverseWearMap[indexCount]][rangeInteger] * number
                    indexCount += 1
                return finalFloat/10

            def getAverageCost(arr):
                indexCount = 0
                cost = 0
                for number in arr:
                    if number > 0:
                        cost += thisWeaponPriceArr[indexCount] * number
                    indexCount += 1
                return cost

            for wearCountEntry in thisWearCountEntries:
                entryCount = 0
                for entry in wearCountEntry:
                    if entry:
                        if entryCount == 0:
                            rangeDelimiter = 'Max'
                        else:
                            rangeDelimiter = 'Min'
                        thisAvgFloat = getAverageFloat(entry, rangeDelimiter)
                        thisAvgCost = getAverageCost(entry)
                        thisAvgProfit = WFH.getAverageValueOfTradeUp(nextRarityWeaponsWearPriceMap, nextRarityUniqueWeapons, thisAvgFloat)
                        thisNetProfitAfterSteam = (thisAvgProfit * 0.86958) - thisAvgCost
                        thisWeaponResults.append([
                            thisWeaponIsStatTrak,
                            thisWeaponName,
                            thisWeaponSkin,
                            rangeDelimiter,
                            entry[0],
                            entry[1],
                            entry[2],
                            entry[3],
                            entry[4],
                            thisWeaponPriceArr[0],
                            thisWeaponPriceArr[1],
                            thisWeaponPriceArr[2],
                            thisWeaponPriceArr[3],
                            thisWeaponPriceArr[4],
                            thisAvgFloat,
                            round(thisAvgCost, 2),
                            round(thisAvgProfit, 2),
                            round(thisNetProfitAfterSteam, 2)
                        ])
                        entryCount += 1

            analysisColumns = ['Stattrak', 'Weapon Name', 'Skin Name', 'Range Delimeter', '#FN', '#MW', '#FT', '#WW', '#BS', '$FN', '$MW', '$FT',
                      '$WW', '$BS', 'floatAvg', 'Avg Cost', 'Avg Profit', 'Net Profit After Steam ($)']
            FH.writeDFToFilepathAsCSV(thisWeaponResults, analysisColumns, '../Analysis/THE_FINAL_SOLUTION/' + caseName.replace(' ', '_') + '/' + thisWeaponStatTrakStr + thisWeaponName.replace(' ', '_') + thisWeaponSkin.replace(' ', '_') + '.csv')

def runAllFinalSolutions():
    for case in os.listdir('../Data/Cases/'):
        case = case.replace('.csv', '').replace(' ', '_')
        if case != 'ALL_CASES':
            if case not in os.listdir('../Analysis/THE_FINAL_SOLUTION/'):
                os.mkdir('../Analysis/THE_FINAL_SOLUTION/' + case + '/')
            if not len(os.listdir('../Analysis/THE_FINAL_SOLUTION/' + case)):
                print("BEGINNING", case.replace('_', ' ').upper())
                theFinalSolution(case.replace('_', ' '))
runAllFinalSolutions()