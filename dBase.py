import sqlite3
import datetime

def DataBase():
    con = sqlite3.connect('Temperature.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE Sensors (id, datetime, value)''')
    con.commit()
    con.close()

def table_filling(temp):
    
    con = sqlite3.connect('Temperature.db')
    cursor = con.cursor()

    info = [temp["Sensor"], datetime.datetime.now(), temp["Temperature"]]
    cursor.execute('INSERT INTO Sensors VALUES (?,?,?)', info)
    
    
    con.commit()
    con.close()