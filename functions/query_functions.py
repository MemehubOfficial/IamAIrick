import pypyodbc
import pandas as pd
from keys import *

steemsql_key = 'uid=Steemit-memehub;pwd=SQfnswpR2GWnenXcTMbz'
def query_steemsql(query):
    connection = pypyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                                'Server=sql.steemsql.com;'
                                'Database=DBSteem;'
                                'uid='+uid+';pwd='+pwd)
    cursor = connection.cursor()

    data = cursor.execute(query).fetchall()
    connection.commit()

    dataframe = pd.DataFrame(data)
    dataframe.columns = [column[0] for column in cursor.description]

    connection.close()
    return dataframe