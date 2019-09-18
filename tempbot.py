import config
import telebot
import serial
import json 
import datetime
from dBase import table_filling

token = '667664175:AAHCAROr2MNqs-J-dv2otjDM6nlgPtBiZDE'

#Работа с COM-портом
ser = serial.Serial()
#Установка параметров COM-порта
ser.baudrate = 9600     #Скорость   
ser.port = 'COM14'      #Порт
ser.timeout = None      #Время, по истечении которого остановится чтение из порта
ser.open()              #Открытие порта 

ser.flushInput()        #Очищает входной буффер
ser.flushOutput()       #Очищает выходной буффер





mybot = telebot.TeleBot(token)

@mybot.message_handler(commands = ["start"])
def start(message):
        mybot.send_message(message, "Hello! I really appreciate your choice! \nUse buttons below!")

@mybot.message_handler(commands = ["sensor 1"])
def sensor_1(message):
        mybot.send_message(message, "asdas")

    

if __name__ == '__main__':
        mybot.polling(none_stop=True)
        temp = ser.readline()
        temp_json = json.loads(temp)
        table_filling(temp_json)
        

