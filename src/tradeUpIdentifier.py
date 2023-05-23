import sys
from tools.floatCombinationGenerator import floatCombinationsGenerator
import controllers.caseController as cC
import controllers.weaponSkinController as wSC
import controllers.wearController as wC
import controllers.rarityController as rC
import tools.tradeUpHelper as tUH

def main():
    # obtain maps
    responseMaps = createTradeUpEfficiencyMaps()
    for index in range(0, len(responseMaps)):
        #idetify stattrak input
        if index == 1:
            findProfitableTradeUps(map, 1)
        else:
            findProfitableTradeUps(map, 0)

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
    allOutputCombinations = []

    ### get combination matrix for later
    fCG = floatCombinationsGenerator()
    floatCombinations = fCG.main()

    containerEntries = cC.getAllContainerNames()
    for containerEntry in containerEntries:
        containerName = containerEntry[0]
        containerIsCollection = containerEntry[1]

        # for all rarities
        rarityArray = rC.rarityArray
        for rarityLevelIndex in range(0, len(rarityArray)):
            rarityLevel = rarityArray[rarityLevelIndex]
            rarityInt = rC.rarityMap[rarityLevel]

            # there are no trade ups for covert weapons OR in the case that searching for consumer in a case returns
            # nothing
            if rarityLevel == 'Covert' or (
                    rarityLevel in ["Consumer", "Industrial"] and containerIsCollection == False):
                continue

            for combination in floatCombinations:
                # get outputs price
                outputMinFloat = combination[0]
                outputMaxFloat = combination[1]
                outputWearOfMinFloat = wC.findWearNameRangeFromValue(outputMinFloat)

                containerSkins = wSC.getAllSkinsForAContainer(containerName)
                outputAvgMin = tUH.getNextRarityLevelAveragePrice(containerSkins, rarityInt, outputWearOfMinFloat, containerIsCollection, statOrSouv)

                # NOT REALLY USEFUL?!?!... write later
                outputWearOfMaxFloat = wC.findWearNameRangeFromValue(outputMaxFloat)

                inputsPrice = tUH.getCombinationInputPrice(map, combination)

                allOutputCombinations.append([outputMinFloat, outputMaxFloat, str()])

        sys.exit('Quit process after first case')




main()