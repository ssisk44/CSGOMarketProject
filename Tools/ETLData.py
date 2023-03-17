import os
import time
import numpy as np
import pandas as pd
import sys
from selenium import webdriver
import requests
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import Tools.WeaponFloatHandler as WeaponFloatHandler


STEAM_APIS_KEY = 'Tms8WF7zHzePsYXVTDdIiPCzAB4'
columnNames = [
    'nameID',
    'market_name',
    'market_hash_name',
    'border_color',
    'image',
    'latest',
    'min',
    'avg',
    'max',
    'mean',
    'median',
    'unstable',
    'unstable_reason',
    'first_seen'
]

def runEntireDataCollectionAndParsingPipeline():
    ### request and receive market data
    makeAndParseSteamApisRequestToData()

    ## parse and prep market data
    mergeAllCasesIntoOne()
    splitAllItemsByItemType()
    addCaseAndWearToAllItems()

    ### Analysis
    getPlainAnalysisForAllCases()


def makeAndParseSteamApisRequestToData():
    # makes call to STEAM APIS to get data on every item in CS:GO with prices
    resSteamApisMapArray = [
        'nameID',
        'market_name',
        'market_hash_name',
        'border_color',
        'image',
        'prices',
    ]
    resPricesSteamApisMapArray = [
        'latest',
        'min',
        'avg',
        'max',
        'mean',
        'median',
        'unstable',
        'unstable_reason',
        'first_seen'
    ]

    res = requests.get('https://api.steamapis.com/market/items/730/?api_key=' + STEAM_APIS_KEY)
    allItemsArr = []
    for item in res.json()['data']:
        itemArr = []
        for key in resSteamApisMapArray:
            if key == 'prices':
                for keyPrices in resPricesSteamApisMapArray:
                    itemArr.append(item['prices'][keyPrices])
            else:
                itemArr.append(item[key])
        allItemsArr.append(itemArr)
    df = pd.DataFrame(data=np.array(allItemsArr), columns=columnNames)
    df.to_csv('Data/unfinishedAllItems.csv', index=False)


def mergeAllCasesIntoOne():
    allCases = []
    for file in os.listdir('Data/Cases/'):
        if file != 'ALL_CASES.csv':
            caseArr = pd.read_csv('Data/Cases/' + file).to_numpy().tolist()
            for item in caseArr:
                allCases.append(item)
    df = pd.DataFrame(data=allCases, columns=['Name', 'Case', 'Skin', 'Rarity'])
    df.to_csv('Data/Cases/ALL_CASES.csv', index=False)


def splitAllItemsByItemType():
    # this function splits items by type (knife, gloves, sticker, weapon) and adds case and rarity to weapons
    allItemsArr = pd.read_csv('Data/unfinishedAllItems.csv').to_numpy()
    glovesArr = []
    knifeArr = []
    stickerArr = []
    weaponArr = []
    totalItems = 0
    parsedItems = 0
    for item in allItemsArr:
        itemName = item[1]
        if 'Sticker |' in itemName:
            stickerArr.append(item)
            parsedItems += 1
        elif 'Knife |' in itemName:
            knifeArr.append(item)
            parsedItems += 1
        elif 'Gloves |' in itemName:
            glovesArr.append(item)
            parsedItems += 1
        elif '|' in itemName:
            # add case and parse wear
            weaponArr.append(item)
            parsedItems += 1
        totalItems += 1

    df = pd.DataFrame(data=np.array(glovesArr), columns=columnNames)
    df.to_csv('Data/Gloves/gloves.csv', index=False)

    df = pd.DataFrame(data=np.array(knifeArr), columns=columnNames)
    df.to_csv('Data/Knifes/knifes.csv', index=False)

    df = pd.DataFrame(data=np.array(stickerArr), columns=columnNames)
    df.to_csv('Data/Stickers/stickers.csv', index=False)

    df = pd.DataFrame(data=np.array(weaponArr), columns=columnNames)
    df.to_csv('Data/Weapons/weaponsMiscellaneous.csv', index=False)

    print("Total Items", totalItems)
    print("# of Items Parsed", parsedItems)


def getCaseAndRarityOfItem(weaponName, skinName):
    allCasesWeaponsArr = pd.read_csv('Data/Cases/ALL_CASES.csv').to_numpy()
    for entry in allCasesWeaponsArr:
        if entry[0] == weaponName and entry[2] == skinName:
            return [entry[1], entry[3]]
    return None


def addCaseAndWearToAllItems():
    # this function finds all CASE ITEMS (not collections) from weaponsMiscellaneous.csv and adds columns for the wear and case, and creates agents csv
    allWeaponsArr = pd.read_csv('Data/Weapons/weaponsMiscellaneous.csv').to_numpy()
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
    df.to_csv('Data/Weapons/weapons.csv', index=False)

    # write agents array
    df = pd.DataFrame(data=np.array(agentsArr), columns=columnNames)
    df.to_csv('Data/Agents/agents.csv', index=False)

    print("Total case items: 646 * 5 (wear per item) * 2 (statrak and normal variant = 6460")
    print("Total items found that matched case items:", caseItemsFoundCounter)


def allTradeUpProfitIdentifier(caseName=''):
    ### Simple execution first -
    # TO DO: add all cases and single case option
    # TO DO: wear averaging combination optimization
    # TO DO: multiple case weapon combination implementation
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
                milSpec.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-4], 2)])
            elif entry[4] == 'Restricted' and entry[5] == stattrak:
                restricted.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-4], 2)])
            elif entry[4] == 'Classified' and entry[5] == stattrak:
                classified.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-4], 2)])
            elif entry[4] == 'Covert' and entry[5] == stattrak:
                covert.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-4], 2)])
        return [milSpec, restricted, classified, covert]

    def filterRarityLevelArrayByWear(rarityLevelArr, wearName):
        filteredArr = []
        for entry in rarityLevelArr:
            if entry[3] == wearName:
                filteredArr.append(entry)
        return filteredArr

    def getAveragePriceOfRarityLevel(rarityLevelArray, wear):
        wearAndRarityByCaseArr = filterRarityLevelArrayByWear(rarityLevelArray, wear)
        print(rarityLevelArray)
        print(wear, wearAndRarityByCaseArr)
        sys.exit()
        price = 0
        for item in wearAndRarityByCaseArr:
            price += item[-1]
        return round(price / len(wearAndRarityByCaseArr), 2)

    def plainTradeUpAnalysis(rarityLevelArray):
        allAnalysis = []
        for rarityLevel in rarityLevelArray:
            thisRarityLevel = rarityLevel[0][4]
            rarityLevelAnalysis = []
            for item in rarityLevel:
                if thisRarityLevel in ["Mil_Spec Grade", "Restricted", "Classified"]:
                    weapon = item[0]
                    skin = item[1]
                    case = item[2]
                    wear = item[3]
                    statrak = item[5]
                    indivPrice = item[-1]
                    tradeUpCost = 10 * item[-1]
                    nextLevel = reverseRarityHierarchyMap[rarityHierarchyMap[thisRarityLevel] + 1]
                    tradeUpProfit = getAveragePriceOfRarityLevel(rarityLevelArray[rarityHierarchyMap[nextLevel]], wear)
                    netProfit = round(tradeUpProfit - tradeUpCost, 2)
                    profitAfterSteam = round(netProfit * (7 / 8), 2)
                    roi = round(profitAfterSteam / tradeUpCost * 100, 2)
                    rarityLevelAnalysis.append(
                        [statrak, weapon, skin, wear, thisRarityLevel, case, indivPrice, tradeUpCost, tradeUpProfit,
                         netProfit, profitAfterSteam, roi])
            allAnalysis.append(rarityLevelAnalysis)
        return allAnalysis

    if caseName == '':
        # see TO DO: implement all cases
        return None

    else:
        caseItemsByRarityNonStatTrak = distributeCaseItemsByRarityName(caseName)
        caseItemsByRarityStatTrak = distributeCaseItemsByRarityName(caseName, 1)
        resultsNonStat = plainTradeUpAnalysis(caseItemsByRarityNonStatTrak)
        resultsStat = plainTradeUpAnalysis(caseItemsByRarityStatTrak)

        results = []

        def normalizeResults():
            for grade in resultsNonStat:
                for entry in grade:
                    results.append(entry)
            for grade in resultsStat:
                for entry in grade:
                    results.append(entry)

        normalizeResults()

        resultsColumns = ['StatTrak', 'Weapon', 'Skin', 'Wear', 'Rarity', 'Case', 'Individual Cost', 'Trade Up Cost',
                          'Profit', 'Net Profit',
                          'Net Profit After Steam Cut', 'ROI %']
        df = pd.DataFrame(data=np.array(results), columns=resultsColumns)
        df = df.sort_values(by=['Net Profit After Steam Cut'], ascending=False)
        df.to_csv('Analysis/Plain/plain' + caseName + '.csv', index=False)
        return None


def getPlainAnalysisForAllCases():
    # begins the plain trade up analysis for all cases
    for case in os.listdir('Data/Cases/'):
        if case != 'ALL_CASES.csv':
            try:
                allTradeUpProfitIdentifier(case.replace('.csv', ''))
            except:
                print('CASE: ', case, "DID NOT COMPLETE DUE TO ERROR")
                continue

def getPlainAnalysisForACase(caseName):
    try:
        allTradeUpProfitIdentifier(caseName)
    except:
        print('CASE: ', caseName, "DID NOT COMPLETE DUE TO ERROR")