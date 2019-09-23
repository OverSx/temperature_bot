import sqlite3
import datetime


def DataBase():
    con = sqlite3.connect('Temperature.db')
    cursor = con.cursor()
    cursor.execute('''CREATE TABLE if not exists Sensor_1 (ID, Datetime, Value)''')
    cursor.execute('''CREATE TABLE if not exists Sensor_2 (ID, Datetime, Value)''')
    con.commit()
    con.close()

def table_filling(tempInfo):
    con = sqlite3.connect('Temperature.db')
    cursor = con.cursor()

    if tempInfo["Sensor"] == 1:
        sql = "SELECT * FROM Sensor_1 WHERE ID=?"
        cursor.execute(sql, (1,))
        if cursor.fetchone() == None:
            index_for_sensor_1 = 1
        else:
            cursor.execute("SELECT * FROM Sensor_1 ORDER BY ID DESC LIMIT 1")
            string_with_value = cursor.fetchone()
            index_for_sensor_1 = string_with_value[0] + 1
        info_sensor_1 = [index_for_sensor_1, datetime.datetime.now(), tempInfo["Temperature"]]
        cursor.execute('INSERT INTO Sensor_1 VALUES (?,?,?)', info_sensor_1)
    
    elif tempInfo["Sensor"] == 2:
        sql = "SELECT * FROM Sensor_2 WHERE ID=?"
        cursor.execute(sql, (1,))
        if cursor.fetchone() == None:
            index_for_sensor_2 = 1
        else:
            cursor.execute("SELECT * FROM Sensor_2 ORDER BY ID DESC LIMIT 1")
            string_with_value = cursor.fetchone()
            index_for_sensor_2 = string_with_value[0] + 1
        info_sensor_2 = [index_for_sensor_2, datetime.datetime.now(), tempInfo["Temperature"]]
        cursor.execute('INSERT INTO Sensor_2 VALUES (?,?,?)', info_sensor_2)

    else:
        exit(0)
    
    
    
    con.commit()
    con.close()

def get_value_temp(number_of_sensor):
    con = sqlite3.connect('Temperature.db')
    cursor = con.cursor()

    if number_of_sensor == 1:
        cursor.execute("SELECT * FROM Sensor_1 ORDER BY ID DESC LIMIT 1")
        string_with_value = cursor.fetchone()
        con.close()
        return string_with_value[2]
    elif number_of_sensor == 2:
        cursor.execute("SELECT * FROM Sensor_2 ORDER BY ID DESC LIMIT 1")
        string_with_value = cursor.fetchone()
        con.close()
        return string_with_value[2]  
    else:
        con.close()
        return "Congrats! You broke my code"