### Float Strategies
# 1) minimizing input float (efficiency) cost to maximize output wear level price [0, 0, 0, 1, 9]
# 2) minimizing input float (exaggeration) to take advantage of overpriced lower wear level [0, 4, 0, 0, 6]


# how can I derive which combinations could yield edge case average floats?
# 1) minimize all floats per level to get the lowest possible output float
# 2) maximize all but the lowest wear level to get highest possible output float

class floatCombinationsGenerator:
    edgeCases = [
        [0.01, .0689],
        [.071, .1489],
        [.1501, .3789],
        [.3801, .4489],
        [.4501, 1]
    ]
    edgeValues = [
        0.07,
        0.15,
        0.38,
        0.45
    ]

    def main(self):
        floatCombinationAnalysisResults = []
        combos = self.generateCombos()
        for combo in combos:
            minimum = 0
            maximum = 0
            lowestWearLevelIndex = self.determineLowestWearLevelInEntry(combo)
            lowestWearLevelTotal = self.getSmallestFloatForWearLevel(lowestWearLevelIndex, combo[lowestWearLevelIndex])
            minimum += lowestWearLevelTotal
            maximum += lowestWearLevelTotal

            # calculate minimum
            minimum += self.calculateRemainingEntry(combo, lowestWearLevelIndex, True)

            # calculate maximum
            maximum += self.calculateRemainingEntry(combo, lowestWearLevelIndex, False)

            result = [round(minimum / 10, 4), round(maximum / 10, 4), combo]
            floatCombinationAnalysisResults.append(result)

        return floatCombinationAnalysisResults

    def generateCombos(self):
        combos = []
        for a in range(0, 10, 1):
            combo = []
            combo.append(a)
            for b in range(0, 10, 1):
                if (a + b) > 10:
                    break
                combo.append(b)
                for c in range(0, 10, 1):
                    if (a + b + c) > 10:
                        break
                    combo.append(c)
                    for d in range(0, 10, 1):
                        if (a + b + c + d) > 10:
                            break
                        combo.append(d)
                        for e in range(0, 10, 1):
                            combo.append(e)
                            if (a + b + c + d + e) == 10:
                                combos.append([a, b, c, d, e])
        return combos

    def determineLowestWearLevelInEntry(self, entry):
        index = 4
        for number in entry[::-1]:
            if number != 0:
                return index
            index -= 1

    def getSmallestFloatForWearLevel(self, index, count):
        return self.edgeCases[index][0] * count

    def getLargestFloatForWearLevel(self, index, count):
        return self.edgeCases[index][1] * count

    def getNextWearLevel(self, entry, index):
        for number in entry[:index:-1]:
            index -= 1
            if number != 0:
                return index
        return False

    def calculateRemainingEntry(self, entry, index, isMin=True):
        total = 0
        for number in entry[:index][::-1]:
            index -= 1
            if number > 0:
                if isMin:
                    total += self.getSmallestFloatForWearLevel(index, number)
                elif not isMin:
                    total += self.getLargestFloatForWearLevel(index, number)
        return total
