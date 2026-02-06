import _mysql_connector

dataBase = _mysql_connector.connect(
    host = 'localhost',
    user = 'asus',
    passwd = 'Asus@123'
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE CRM_DB")

print("DB created sucessfully!!")