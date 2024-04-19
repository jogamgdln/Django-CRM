# Install-Mysql-on-Computer
# https://dev.mysql.com/downloads/installer
# pip install mysql
# pip install mysql-connector
# pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'clave123'

    ) 

nombreBd = input('Digita el nombre para la base de datos: ')
print()

# prpare a cursor object
cursorObject = dataBase.cursor()

# Crate a database
cursorObject.execute('CREATE DATABASE ' + nombreBd)

print('All Done!')

