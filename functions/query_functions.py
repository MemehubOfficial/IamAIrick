import pypyodbc
import pandas as pd
from keys import *
import time

def stopWatch(value):
    '''From seconds to Days;Hours:Minutes;Seconds'''

    valueD = (((value/365)/24)/60)
    Days = int (valueD)

    valueH = (valueD-Days)*365
    Hours = int(valueH)

    valueM = (valueH - Hours)*24
    Minutes = int(valueM)

    valueS = (valueM - Minutes)*60
    Seconds = int(valueS)


    return str(Days)+"D:"+str(Hours)+"H:"+str(Minutes)+"M:"+str(Seconds)+"S"

#Queries steemsql with the query passed as a param
#returns query data as a dataframe
def query_steemsql(query):
    connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                'Server=sql.steemsql.com;'
                                'Database=DBSteem;'
                                'uid='+uid+';pwd='+pwd)

    now = time.time()

    # cursor = connection.cursor()
    # data = cursor.execute(query).fetchall()
    # dataframe = pd.DataFrame(data)

    dataframe = pd.read_sql(query, connection)
    connection.commit()
    

    if dataframe.empty:
        connection.close()
        return print("Query is empty")
    # else:
    #     dataframe.columns = [column[0] for column in cursor.description]

    connection.close()

    query_time = time.time() - now

    if query_time > 10:
        print("Query Time was: "+stopWatch(query_time))
    print("The number of entries found: "+str(len(dataframe.index)))
    return dataframe