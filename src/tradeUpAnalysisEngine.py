# def allTradeUpProfitIdentifier(caseName=''):
#     ### Simple execution first -
#     # TO DO: add all cases and single case option
#     # TO DO: wear averaging combination optimization
#     # TO DO: multiple case weapon combination implementation
#     rarityHierarchyMap = {
#         "Mil_Spec Grade": 0,
#         "Restricted": 1,
#         "Classified": 2,
#         "Covert": 3
#     }
#     reverseRarityHierarchyMap = {
#         0: "Mil_Spec Grade",
#         1: "Restricted",
#         2: "Classified",
#         3: "Covert"
#     }
#     weaponWearArray = [
#         'Battle-Scarred',
#         'Well-Worn',
#         'Field-Tested',
#         'Minimal Wear',
#         'Factory New'
#     ]
#
#     def getAllItemsForACase(caseName):
#         allItems = pd.read_csv('tmp/Weapons/weapons.csv').to_numpy()
#         caseItems = []
#         for entry in allItems:
#             if entry[2] == caseName:
#                 caseItems.append(entry)
#         return caseItems
#
#     def distributeCaseItemsByRarityName(caseName, stattrak=0):
#         caseItems = getAllItemsForACase(caseName)
#         milSpec = []
#         restricted = []
#         classified = []
#         covert = []
#         for entry in caseItems:
#             if entry[4] == 'Mil_Spec Grade' and entry[5] == stattrak:
#                 milSpec.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-4], 2)])
#             elif entry[4] == 'Restricted' and entry[5] == stattrak:
#                 restricted.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-4], 2)])
#             elif entry[4] == 'Classified' and entry[5] == stattrak:
#                 classified.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-4], 2)])
#             elif entry[4] == 'Covert' and entry[5] == stattrak:
#                 covert.append([entry[0], entry[1], entry[2], entry[3], entry[4], entry[5], round(entry[-4], 2)])
#         return [milSpec, restricted, classified, covert]
#
#     def filterRarityLevelArrayByWear(rarityLevelArr, wearName):
#         filteredArr = []
#         for entry in rarityLevelArr:
#             if entry[3] == wearName:
#                 filteredArr.append(entry)
#         return filteredArr
#
#     def getAveragePriceOfRarityLevel(rarityLevelArray, wear):
#         wearAndRarityByCaseArr = filterRarityLevelArrayByWear(rarityLevelArray, wear)
#         price = 0
#         for item in wearAndRarityByCaseArr:
#             price += item[-1]
#         return round(price / len(wearAndRarityByCaseArr), 2)
#
#     def plainTradeUpAnalysis(rarityLevelArray):
#         allAnalysis = []
#         for rarityLevel in rarityLevelArray:
#             thisRarityLevel = rarityLevel[0][4]
#             rarityLevelAnalysis = []
#             for item in rarityLevel:
#                 if thisRarityLevel in ["Mil_Spec Grade", "Restricted", "Classified"]:
#                     weapon = item[0]
#                     skin = item[1]
#                     case = item[2]
#                     wear = item[3]
#                     statrak = item[5]
#                     indivPrice = item[-1]
#                     tradeUpCost = 10 * item[-1]
#                     nextLevel = reverseRarityHierarchyMap[rarityHierarchyMap[thisRarityLevel] + 1]
#                     tradeUpProfit = getAveragePriceOfRarityLevel(rarityLevelArray[rarityHierarchyMap[nextLevel]], wear)
#                     netProfit = round(tradeUpProfit - tradeUpCost, 2)
#                     profitAfterSteam = round(netProfit * (7 / 8), 2)
#                     roi = round(profitAfterSteam / tradeUpCost * 100, 2)
#                     rarityLevelAnalysis.append(
#                         [statrak, weapon, skin, wear, thisRarityLevel, case, indivPrice, tradeUpCost, tradeUpProfit,
#                          netProfit, profitAfterSteam, roi])
#             allAnalysis.append(rarityLevelAnalysis)
#         return allAnalysis
#
#     if caseName == '':
#         # see TO DO: implement all cases
#         return None
#
#     else:
#         caseItemsByRarityNonStatTrak = distributeCaseItemsByRarityName(caseName)
#         caseItemsByRarityStatTrak = distributeCaseItemsByRarityName(caseName, 1)
#         resultsNonStat = plainTradeUpAnalysis(caseItemsByRarityNonStatTrak)
#         resultsStat = plainTradeUpAnalysis(caseItemsByRarityStatTrak)
#
#         results = []
#
#         def normalizeResults():
#             for grade in resultsNonStat:
#                 for entry in grade:
#                     results.append(entry)
#             for grade in resultsStat:
#                 for entry in grade:
#                     results.append(entry)
#
#         normalizeResults()
#
#         resultsColumns = ['StatTrak', 'Weapon', 'Skin', 'Wear', 'Rarity', 'Case', 'Individual Cost', 'Trade Up Cost',
#                           'Profit', 'Net Profit',
#                           'Net Profit After Steam Cut', 'ROI %']
#         df = pd.DataFrame(data=np.array(results), columns=resultsColumns)
#         df = df.sort_values(by=['Net Profit After Steam Cut'], ascending=False)
#         df.to_csv('analyis/Plain/plain' + caseName + '.csv', index=False)
#         return None
#
#
# def getPlainAnalysisForAllCases():
#     # begins the plain trade up analysis for all cases
#     for case in os.listdir('tmp/Cases/'):
#         if case != 'ALL_CASES.csv':
#             try:
#                 allTradeUpProfitIdentifier(case.replace('.csv', ''))
#             except:
#                 print('CASE: ', case, "DID NOT COMPLETE DUE TO ERROR")
#                 continue
#
#
# def getPlainAnalysisForACase(caseName):
#     try:
#         allTradeUpProfitIdentifier(caseName)
#     except:
#         print('CASE: ', caseName, "DID NOT COMPLETE DUE TO ERROR")