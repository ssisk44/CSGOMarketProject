import database.query as Query

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
reverseWearRangeMap = {
    [0.00, 0.0699999999999999999999999999999999999]: 'Factory New',
    [0.07, 0.149999999999999999999999999999999999]: 'Minimal Wear',
    [0.15, 0.379999999999999999999999999999999999]: 'Field-Tested',
    [0.38, 0.449999999999999999999999999999999999]: 'Well-Worn',
    [0.45, 1.00]: 'Battle-Scarred'
}

# def getWearNameByID(id: int):
#     res = Query.executeSingularQuery('SELECT wearName from static_data.wear WHERE wearID = ' + str(id) + ';')
#     return res[0][0]
#
# def getWearFloatMinMaxByID(id: int):
#     res = Query.executeSingularQuery('SELECT wearFloatMin,wearFloatMax from static_data.wear WHERE wearID = ' + str(id) + ';')
#     return [res[0][0], res[0][1]]
#
# def getWearIDByWearName(wearName: str):
#     sql = "SELECT wearID FROM static_data.wear WHERE wearName = '" + wearName + "';"
#     res = Query.executeSingularQuery(sql)
#     return res[0][0]
#
