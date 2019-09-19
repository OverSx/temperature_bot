import sqlite3
import datetime

first_time_1 = True
first_time_2 = True

def DataBase():
    con = sqlite3.connect('Temperature.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE Sensor_1 (ID, Datetime, Value)''')
    cursor.execute('''CREATE TABLE Sensor_2 (ID, Datetime, Value)''')
    con.commit()
    con.close()

def table_filling(tempInfo):
    
    con = sqlite3.connect('Temperature.db')
    cursor = con.cursor()

    
    if tempInfo["Sensor"] == 1:
        
        if first_time_1 == True:
            index_for_sensor_1 = 0
            first_time_1 = False
        
        index_for_sensor_1 += 1
        info_sensor_1 = [index_for_sensor_1, datetime.datetime.now(), tempInfo["Temperature"]]
        cursor.execute('INSERT INTO Sensor_1 VALUES (?,?,?)', info_sensor_1)
    
    elif tempInfo["Sensor"] == 2:
        
        if first_time_2 == True:
            index_for_sensor_2 = 0
            first_time_2 = False
        
        index_for_sensor_2 += 1
        info_sensor_2 = [index_for_sensor_2, datetime.datetime.now(), tempInfo["Temperature"]]
        cursor.execute('INSERT INTO Sensor_2 VALUES (?,?,?)', info_sensor_2)

    else:
        return 0
    
    
    
    con.commit()
    con.close()