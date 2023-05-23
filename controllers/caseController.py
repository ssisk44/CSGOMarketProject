import database.query as Query
from tools.databaseOutputFormatter import *


def getAllContainers():
    """retrieve cases and collections"""
    res = Query.executeSingularQuery('SELECT * from static_data.cases;')
    retArray = []
    for array in res:
        a = []
        for entry in array:
            a.append(entry)
        retArray.append(a)
    return retArray


def getContainerIndexByName(name: str):
    """"""
    sql = "SELECT c_id from static_data.cases where c_name = '" + str(name) + "';"
    res = Query.executeSingularQuery(sql)
    return res[0][0] - 1


def getAllContainerNames(isCase: int = None):
    sql = "SELECT c_name, c_is_collection FROM static_data.cases"
    if isCase is not None:
        sql += " where c_is_collection = '" + str(isCase) + "'"
    sql += ';'
    res = Query.executeSingularQuery(sql)
    formattedRes = formatArrayOutput(res)
    return formattedRes
