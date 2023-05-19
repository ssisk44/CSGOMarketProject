import database.query as Query

def getAllContainers():
    """retrieve cases and collections"""
    res = Query.executeSingularQuery('SELECT * from static_data.case;')
    retArray = []
    for array in res:
        a = []
        for entry in array:
            a.append(entry)
        retArray.append(a)
    return retArray