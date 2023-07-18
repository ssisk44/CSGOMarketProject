def getAdjustedFloat(minFloatCap, floatRange, outputWear):
    adjustedFloat = round((outputWear * floatRange) + minFloatCap, 5)
    return adjustedFloat
