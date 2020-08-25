
#### lets import a data set from mySQL to python

#import 
import mysql.connector
from mysql.connector import (connection)
import pandas as pd

#open the door between pyhton and the database
cnx = connection.MySQLConnection(user = 'root',password = 'descobri93', host ='localhost', database = 'stand_virtual',auth_plugin='mysql_native_password')

#verify that is connected
cnx.is_connected()

# define the object (cursor) we will use to interact with the database
cursor = cnx.cursor()

#define our query
query = ("SELECT * FROM stand_virtual.dataset;")

cursor.execute(query)

results = cursor.fetchall()


#we now have our dataset from SQL in a list of lists.

cols= ['Car_ID','Brand','Model','Year','Km','Doors','Seats','TransmissionNr','Fuel','Power','Cylinder Engine','Transmission','AC','Condition','Price']

#Insert in a DataFrame and insert columns names
df = pd.DataFrame(results, columns= cols)

df.to_csv('df_from_sql.csv')

print(results[0])