import sys
from database.connection import Connection

def executeSingularQuery(query, debug=False, db='static_data'):
    connection = Connection(db)
    connection.connect()
    connection.start_transaction()
    try:
        res = connection.execute_query(query)
        connection.commit_transaction()
        if debug:
            print('Query executed and transaction committed!')
    except:
        connection.rollback_transaction()
        sys.exit('Database query rolled back! Grrrrr')
    connection.disconnect()
    if res:
        return res
