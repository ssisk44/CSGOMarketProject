import database.query as Query
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

### needs a function to search range qualifier
reverseWearRange = [
    [0.00, 0.0699999999999999999999999999999999999],
    [0.07, 0.149999999999999999999999999999999999],
    [0.15, 0.379999999999999999999999999999999999],
    [0.38, 0.449999999999999999999999999999999999],
    [0.45, 1.00]
]

def findWearNameRangeFromValue(value: float):
    """
    TESTED AND WORKING :)
    :param value:
    :return:
    """
    for index in range(0, len(reverseWearRange)):
        floatRange = reverseWearRange[index]
        if floatRange[0] <= value < floatRange[1]:
            return reverseWearMap[index]
