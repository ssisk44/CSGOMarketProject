import database.query as Query

def getRarityNameByRarityID(rarityID: int):
    res = Query.executeSingularQuery('SELECT rarityName from static_data.rarity WHERE rarityID = ' + str(rarityID) + ';')
    return res[0][0]

def getRarityIDByRarityName(rarityName: str):
    sql = "SELECT rarityID FROM static_data.rarity WHERE rarityName = '" + rarityName + "';"
    res = Query.executeSingularQuery(sql)
    return res[0][0]