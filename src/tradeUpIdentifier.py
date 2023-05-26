import sys
from tools.floatCombinationGenerator import floatCombinationsGenerator
import controllers.caseController as cC
import controllers.weaponSkinController as wSC
import controllers.wearController as wC
import controllers.rarityController as rC
import tools.tradeUpHelper as tUH
import tools.fileHandler as fH

# if a positive most efficient trade up for rarity level is found, technically other weapons could present themselves as profitable as well
# finding substitute same tier weapons for float price?
def main():
    # obtain maps
    responseMaps = createTradeUpEfficiencyMaps()
    for index in range(0, len(responseMaps)):
        #idetify stattrak input
        if index == 1:
            findProfitableTradeUps(responseMaps[1], 1)
        else:
            findProfitableTradeUps(responseMaps[0], 0)

def createTradeUpEfficiencyMaps():
    ### GET MOST EFFICIENT TRADE UP WEAPON MATRICES

    # for all cases
    allCaseValueMap = {}
    allCaseStatOrSouvValueMap = {}
    containerEntries = cC.getAllContainerNames()
    for containerEntry in containerEntries:
        containerName = containerEntry[0]
        allCaseValueMap[containerName] = {}
        allCaseStatOrSouvValueMap[containerName] = {}
        containerWeapons = wSC.getAllSkinsForAContainer(containerName)
        containerIsCollection = containerEntry[1]

        # for all rarities
        rarityArray = rC.rarityArray
        for rarityLevelIndex in range(0, len(rarityArray)):
            rarityLevel = rarityArray[rarityLevelIndex]
            rarityInt = rC.rarityMap[rarityLevel]

            # there are no trade ups for covert weapons OR in the case that searching for consumer in a case returns
            # nothing
            if rarityLevel == 'Covert' or (rarityLevel in ["Consumer", "Industrial"] and containerIsCollection == False):
                continue

            allCaseValueMap[containerName][rarityLevel] = {}
            allCaseStatOrSouvValueMap[containerName][rarityLevel] = {}

            # for all wears
            wearArray = wC.wearArray
            for wearLevelIndex in range(0, len(wearArray)):
                wearLevel = wearArray[wearLevelIndex]

                # for stattrak or souvenir and not
                nonStatOrSouvEntries, statOrSouvEntries = None, None
                for statOrSouvValue in range(0, 2, 1):
                    if statOrSouvValue == 0:
                        nonStatOrSouvEntries = wSC.getEntries(containerWeapons, rarityInt, wearLevel,
                                                              containerIsCollection, statOrSouvValue)
                    else:
                        statOrSouvEntries = wSC.getEntries(containerWeapons, rarityInt, wearLevel,
                                                           containerIsCollection, statOrSouvValue)
                # TO DO: add float range incompleteness scanning to cheapest tradeup
                nonStatOrSouvCheapestPrice = tUH.getCheapestTradeUpChoice(nonStatOrSouvEntries)
                if nonStatOrSouvCheapestPrice is not None:
                    allCaseValueMap[containerName][rarityLevel][wearLevel] = nonStatOrSouvCheapestPrice

                statOrSouvCheapestPrice = tUH.getCheapestTradeUpChoice(statOrSouvEntries)
                if statOrSouvCheapestPrice is not None:
                    allCaseStatOrSouvValueMap[containerName][rarityLevel][wearLevel] = statOrSouvCheapestPrice

    return [allCaseValueMap, allCaseStatOrSouvValueMap]




def findProfitableTradeUps(map, statOrSouv = 0):
    """
    Cycles through pre-made efficient weapons map to calculate the efficiency of each trade up combination
    :param map:
    :param statOrSouv:
    :return:
    """
    allOutputCombinations = []

    ### get combination matrix for later
    fCG = floatCombinationsGenerator()
    floatCombinations = fCG.main()

    for caseName in map:
        for rarityLevelName in map[caseName]:
            containerSkins = wSC.getAllSkinsForAContainer(caseName)
            isCase = containerSkins[0][-2]  # ASSUMES THE FIRST WEAPON IS A STATTRAK ENTRY
            containerIsCollection = False
            if isCase == 0:
                containerIsCollection = True

            for combination in floatCombinations:
                comboEntry = []
                # get outputs price
                outputMinFloat = combination[0]
                outputMaxFloat = combination[1]
                outputWearOfMinFloat = wC.findWearNameRangeFromValue(outputMinFloat)

                # get average price of next rarity level for output wear in the same case
                rarityInt = rC.rarityMap[rarityLevelName]
                outputAvgMin = tUH.getNextRarityLevelAveragePrice(containerSkins, rarityInt, outputWearOfMinFloat, containerIsCollection, statOrSouv)

                # NOT REALLY USEFUL?!?!... write later
                outputWearOfMaxFloat = wC.findWearNameRangeFromValue(outputMaxFloat)

                inputsPrice = tUH.getCombinationInputsPrice(map[caseName], combination, rarityLevelName)
                print(inputsPrice, "\n")

                comboEntry.append(outputMinFloat)
                comboEntry.append(outputMaxFloat)
                for number in combination[2]:
                    comboEntry.append(number)
                comboEntry.append(inputsPrice)
                comboEntry.append(outputAvgMin)
                comboEntry.append(round(outputAvgMin-inputsPrice, 2))
                allOutputCombinations.append(comboEntry)
        fH.writeDFToFilepathAsCSV(allOutputCombinations, None, '../tmp/test.csv')
        print(allOutputCombinations)
        sys.exit('Quit process after first case')




main()