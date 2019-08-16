import pandas as pd
import functions.func as func
import time
import config
import pypyodbc as db
from contextlib import contextmanager

@contextmanager
def open_connection():
    try:
        connection = db.connect('Driver={ODBC Driver 17 for SQL Server};'
                                'Server=sql.steemsql.com;'
                                'Database=DBSteem;'
                                'uid='+config.steemsql_uid+';pwd='+config.steemsql_pwd)
        yield connection
    finally:
        connection.close()

#Queries steemsql with the query passed as a param
#returns query data as a dataframe
def query(query):
    now = time.time()

    #connection = open_connection()

    # cursor = connection.cursor()
    # data = cursor.execute(query).fetchall()
    # dataframe = pd.DataFrame(data)

    with open_connection() as connection:
        dataframe = pd.read_sql(query, connection)

    #connection.close()

    if dataframe.empty:
        print("Query is empty")
        return None
    # else:
    #     dataframe.columns = [column[0] for column in cursor.description]

    query_time = time.time() - now

    if query_time > 30:
        print("Query Time was: "+func.stopWatch(query_time))
    print("The number of entries found: "+str(len(dataframe.index)))
    return dataframe

