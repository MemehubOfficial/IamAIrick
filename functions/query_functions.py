import pandas as pd
from functions.stopWatch import stopWatch
import time
from keys import *
import pypyodbc as db

def open_connection():
    return db.connect('Driver={ODBC Driver 17 for SQL Server};'
                                'Server=sql.steemsql.com;'
                                'Database=DBSteem;'
                                'uid='+uid+';pwd='+pwd)

#Queries steemsql with the query passed as a param
#returns query data as a dataframe
def query_steemsql(query, connection):
    now = time.time()

    # cursor = connection.cursor()
    # data = cursor.execute(query).fetchall()
    # dataframe = pd.DataFrame(data)

    dataframe = pd.read_sql(query, connection)
    connection.commit()

    if dataframe.empty:
        connection.close()
        print("Query is empty")
        return None
    # else:
    #     dataframe.columns = [column[0] for column in cursor.description]

    query_time = time.time() - now

    if query_time > 30:
        print("Query Time was: "+stopWatch(query_time))
    print("The number of entries found: "+str(len(dataframe.index)))
    return dataframe