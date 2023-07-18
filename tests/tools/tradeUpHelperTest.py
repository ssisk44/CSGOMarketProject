import sys
import unittest
import tools.tradeUpHelper as tUH
import controllers.weaponSkinController as wSC
import tools.staticAssets as testAssets


class TradeUpHelperTest(unittest.TestCase):
    ### getNextRarityLevelAveragePrice
    containerSkins = wSC.getAllSkinsForAContainer('Revolution Case')
    revContainerArray = testAssets.getTestRevolutionCaseArray()
    psuedoRevEfficiencyMap = testAssets.getTestPseudoRevolutionEfficiencyMap()

    def testGetNextRarityLevelAveragePrice(self):
        outputAvgMin = tUH.getNextRarityLevelAveragePrice(self.containerSkins, 4, 'Factory New', 0, 1, True)
        self.assertEqual(outputAvgMin, 822.0, "Should be 822.0")


    ### getCombinationInputPrice
    def testGetCombinationInputsPrice(self):
        expectedTotal = ((self.psuedoRevEfficiencyMap['Revolution Case']['Mil-Spec']['Well-Worn'][-1]) + (
                9 * self.psuedoRevEfficiencyMap['Revolution Case']['Mil-Spec']['Battle-Scarred'][-1])) / 10
        res = tUH.getCombinationInputsPrice(self.psuedoRevEfficiencyMap['Revolution Case'], ['', '', [0, 1, 2, 3, 4]],
                                            'Mil-Spec')
        self.assertEqual(20, res, "Should be 20")


if __name__ == '__main__':
    unittest.main()
