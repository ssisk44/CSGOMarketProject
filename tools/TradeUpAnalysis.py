import os
import pandas as pd
import src.weaponFloatDataRetriever as WFH
import tools.PriceHandler as PH
import tools.fileHandler as FH


# https://csgoskins.gg/markets/market-csgo

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
            # WARNING -> if a weapon hasnt sold in a while the lack of tmp will cause an error ex. FN Fire Serpent -> manual fixes for now
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
            # manual fix mentioned above implemented here
            if thisWeaponName in ['AWP', 'P2000'] and thisWeaponSkin in ['Graphite', 'Ocean Foam'] and thisWeaponIsStatTrak:
                nextRarityWeaponsWearPriceMap = {'Fire Serpent': {'Factory New': 0.00, 'Minimal Wear': 1849.4, 'Field-Tested': 1636.78, 'Well-Worn': 1272.74, 'Battle-Scarred': 1168.41}, 'Golden Koi': {'Factory New': 111.09, 'Minimal Wear': 81.02, 'Field-Tested': None, 'Well-Worn': None, 'Battle-Scarred': None}}

            nextRarityUniqueWeapons = []
            for weapon in nextRarityUniqueWeaponSkinWear:
                if [weapon[0], weapon[1]] not in nextRarityUniqueWeapons:
                    nextRarityUniqueWeapons.append([weapon[0], weapon[1]])

            # TIME FOR THE HEAVY LIFTING >:D
            # get item float cap
            thisFloatCap = WFH.getFloatCapsByWeaponNameSkinName(thisWeaponName, thisWeaponSkin,
                                                                '../tmp/Float/floatCaps.csv')

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

            def getAverageFloat(arr, wearDelimiter):
                wearDelimiterValue = 0
                if wearDelimiter == 'max':
                    wearDelimiterValue = 1

                finalFloat = 0.00
                indexCount = 0
                for number in arr:
                    if number > 0:
                        finalFloat += thisWearRangeMap[reverseWearMap[indexCount]][wearDelimiterValue] * number
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

            # wearMin/Max integers serve as the array range and indexes for values price value combinations
            # get this weapons wear combinations
            # thisWearCountEntries = []
            # for section in wearCountSections[thisWearMinInteger: thisWearMaxInteger + 1]:
            #     for thisSectionWearCombinations in section[thisWearMinInteger: thisWearMaxInteger + 1]:
            #         thisWearCountEntries.append(thisSectionWearCombinations[0])
            # debug
            # print(thisWeaponPriceArr)
            def makeWearCountEntryCombinations():
                wearComboVariables = ['a', 'b', 'c', 'd','e']
                wearInavailability = []
                for index in range(0, len(thisWeaponPriceArr)):
                    if thisWeaponPriceArr[index] == None:
                        wearInavailability.append(wearComboVariables[index])
                combos = []
                for a in range(0, 11, 1):
                    if thisWeaponPriceArr[0] == None and a>0:
                        break
                    for b in range(0, 11, 1):
                        if thisWeaponPriceArr[1] == None and b > 0:
                            break
                        for c in range(0, 11, 1):
                            if thisWeaponPriceArr[2] == None and c > 0:
                                break
                            for d in range(0, 11, 1):
                                if thisWeaponPriceArr[3] == None and d > 0:
                                    break
                                for e in range(0, 11, 1):
                                    if thisWeaponPriceArr[4] == None and e > 0:
                                        break
                                    if (a + b + c + d + e) == 10:
                                        combos.append([[a, b, c, d, e], 'min'])
                                        combos.append([[a, b, c, d, e], 'max'])
                return combos
            thisWearCountEntries = makeWearCountEntryCombinations()

            for wearCountEntry in thisWearCountEntries:
                thisAvgFloat = getAverageFloat(wearCountEntry[0], wearCountEntry[1])
                thisAvgCost = getAverageCost(wearCountEntry[0])
                thisAvgProfit = WFH.getAverageValueOfTradeUp(nextRarityWeaponsWearPriceMap, nextRarityUniqueWeapons, thisAvgFloat)
                thisNetProfitAfterSteam = (thisAvgProfit * 0.86958) - thisAvgCost
                thisWeaponResults.append([
                    thisWeaponIsStatTrak,
                    thisWeaponName,
                    thisWeaponSkin,
                    wearCountEntry[1],
                    wearCountEntry[0][0],
                    wearCountEntry[0][1],
                    wearCountEntry[0][2],
                    wearCountEntry[0][3],
                    wearCountEntry[0][4],
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

            analysisColumns = ['Stattrak', 'Weapon Name', 'Skin Name', 'Range Delimiter',  '#FN', '#MW', '#FT', '#WW', '#BS', '$FN', '$MW', '$FT',
                      '$WW', '$BS', 'floatAvg', 'Avg Cost', 'Avg Profit', 'Net Profit After Steam ($)']
            FH.writeDFToFilepathAsCSV(thisWeaponResults, analysisColumns, '../analyis/THE_FINAL_SOLUTION/' + caseName.replace(' ', '_') + '/' + thisWeaponStatTrakStr + thisWeaponName.replace(' ', '_') + thisWeaponSkin.replace(' ', '_') + '.csv', True)

def runAllFinalSolutions():
    for case in os.listdir('../tmp/Cases/'):
        case = case.replace('.csv', '').replace(' ', '_')
        if case != 'ALL_CASES':
            if case not in os.listdir('../analyis/THE_FINAL_SOLUTION/'):
                os.mkdir('../analyis/THE_FINAL_SOLUTION/' + case + '/')
            if not len(os.listdir('../analyis/THE_FINAL_SOLUTION/' + case)):
                print("BEGINNING", case.replace('_', ' ').upper())
                theFinalSolution(case.replace('_', ' '))


def collectFinalSolutionResults():
    runAllFinalSolutions()
    finalSolutionPath = '../analyis/THE_FINAL_SOLUTION/'
    allResults = []
    for caseDirectory in os.listdir(finalSolutionPath):
        for file in os.listdir(finalSolutionPath + caseDirectory):
            fileContents = pd.read_csv(finalSolutionPath + caseDirectory + '/' + file).to_numpy().tolist()
            for entry in fileContents:
                if entry[-1] > 0: ############
                    allResults.append(entry)
    resultsColumns = ['Stattrak', 'Weapon Name', 'Skin Name', 'Range Delimeter', '#FN', '#MW', '#FT', '#WW', '#BS',
                       '$FN', '$MW', '$FT',
                       '$WW', '$BS', 'floatAvg', 'Avg Cost', 'Avg Profit', 'Net Profit After Steam ($)']
    FH.writeDFToFilepathAsCSV(allResults, resultsColumns, '../analyis/AllPositiveYieldResults.csv', sort=True)



collectFinalSolutionResults()