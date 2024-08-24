import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'L01027046@hasibjan',
)


# create a cursor object
cursorobject = dataBase.cursor()


# create a database 

cursorobject.execute("CREATE DATABASE crmweb")


print("all done!")