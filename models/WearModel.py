import database.query as Query

def getWearNameByID(id: int):
    res = Query.executeSingularQuery('SELECT wearName from static_data.wear WHERE wearID = ' + str(id) + ';')
    return res[0][0]

def getWearFloatMinMaxByID(id: int):
    res = Query.executeSingularQuery('SELECT wearFloatMin,wearFloatMax from static_data.wear WHERE wearID = ' + str(id) + ';')
    return [res[0][0], res[0][1]]

def getWearIDByWearName(wearName: str):
    sql = "SELECT wearID FROM static_data.wear WHERE wearName = '" + wearName + "';"
    res = Query.executeSingularQuery(sql)
    return res[0][0]

