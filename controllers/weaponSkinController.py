from typing import List

import database.query as Query
from tools.databaseOutputFormatter import *


def getAllSkinsForAContainer(container: str):
    """retrieve cases and collections"""
    sql = "SELECT * from static_data.weapon_skins where ws_case_name = '" + container + "';"
    res = Query.executeSingularQuery(sql)
    formattedRes = formatArrayOutput(res)
    return formattedRes


def getEntriesByCaseAndRarity(caseName: str, rarity_id: int):
    sql = "SELECT * from static_data.weapon_skins where ws_case_name= '" + caseName + "' and ws_r_id = '" + str(
        rarity_id) + "';"
    res = Query.executeSingularQuery(sql)
    formattedRes = formatArrayOutput(res)
    return formattedRes


def getFloatRangeFromEntry(entry):
    """should only return one float entry per request, hard to identify gun float parings if otherwise"""
    return entry[5:7]


def getUniqueWeaponEntriesByCaseAndRarity(caseName: str, rarity_id: int):
    """ returns a singular weapon per wear spectrum in a ase and rarity, most likely multiple outputs"""
    sql = "SELECT * from static_data.weapon_skins where ws_case_name= '" + caseName + "' and ws_r_id = '" + str(
        rarity_id) + "';"
    res = Query.executeSingularQuery(sql)
    formattedRes = formatArrayOutput(res)
    uniqueRes = filterIndividualWeaponOutputs(formattedRes)
    return uniqueRes


def getEntriesByWearLevel(entries: List[list], wear: str):
    """
    TESTED AND WORKING
    :param entries:
    :param wear:
    :return:
    """
    retArr = []
    for entry in entries:
        if entry[4] == wear:
            retArr.append(entry)
    return retArr


def getEntriesByRarityLevel(entries: List[list], rarity_id: int):
    """
    TESTED AND WORKING
    :param entries:
    :param rarity_id:
    :return:
    """
    retArr = []
    r_id = str(rarity_id)
    for entry in entries:
        if entry[7] == r_id:
            retArr.append(entry)
    return retArr


def splitEntriesByStatOrSouvValue(entries):
    regularArr = []
    statOrSouvArr = []
    for entry in entries:
        if entry[8] == 1 or entry[9] == 1:
            statOrSouvArr.append(entry)
        else:
            regularArr.append(entry)
    return [regularArr, statOrSouvArr]


def getEntries(entries: List[list], rarity: int, wear: str, isCollection: int, statOrSouv: int, debug = False):
    """
    TESTED AND WORKING
    :param entries:
    :param rarity:
    :param wear:
    :param isCollection:
    :param statOrSouv:
    :return:
    """
    if debug:
        print(rarity, wear, isCollection, statOrSouv)
    retEntries = []
    for entry in entries:
        # for cases
        if isCollection == 0:
            if debug:
                print(entry)
                print("\n")
            if str(entry[7]) == str(rarity) and str(entry[4]) == str(wear) and str(entry[8]) == str(statOrSouv):
                retEntries.append(entry)

        #for collections
        elif isCollection == 1:
            if str(entry[7]) == str(rarity) and str(entry[4]) == str(wear) and str(entry[9]) == str(statOrSouv):
                retEntries.append(entry)

    return retEntries
