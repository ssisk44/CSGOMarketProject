import database.query as Query
from tools.databaseOutputFormatter import *

def getAllSkinsForAContainer(container: str):
    """retrieve cases and collections"""
    sql ="SELECT * from static_data.weapon_skins where ws_case_name = '" + container + "';"
    res = Query.executeSingularQuery(sql)
    return res

def getEntriesByCaseAndRarity(caseName: str, rarity_id: int):
    sql = "SELECT * from static_data.weapon_skins where ws_case_name= '" + caseName + "' and ws_r_id = '" + str(rarity_id) + "';"
    res = Query.executeSingularQuery(sql)
    formattedRes = formatArrayOutput(res)
    return formattedRes

def getFloatRangeFromEntry(entry):
    """should only return one float entry per request, hard to identify gun float parings if otherwise"""
    return entry[5:7]

def getUniqueWeaponEntriesByCaseAndRarity(caseName: str, rarity_id: int):
    """ returns a singular weapon per wear spectrum in a ase and rarity, most likely multiple outputs"""
    sql = "SELECT * from static_data.weapon_skins where ws_case_name= '" + caseName + "' and ws_r_id = '" + str(rarity_id) + "';"
    res = Query.executeSingularQuery(sql)
    formattedRes = formatArrayOutput(res)
    uniqueRes = filterIndividualWeaponOutputs(formattedRes)
    return uniqueRes

