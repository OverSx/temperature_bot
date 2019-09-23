from telegram.ext import Updater
from telegram.ext import CommandHandler
import serial
import json 
import datetime
from threading import Thread
from dBase import table_filling
from dBase import DataBase
from dBase import get_value_temp


token = '667664175:AAHCAROr2MNqs-J-dv2otjDM6nlgPtBiZDE'

try:
        #Работа с COM-портом
        ser = serial.Serial()
        #Установка параметров COM-порта
        ser.baudrate = 9600     #Скорость   
        ser.port = 'COM14'      #Порт
        ser.timeout = None      #Время, по истечении которого остановится чтение из порта
        ser.open()              #Открытие порта 

        ser.flushInput()        #Очищает входной буффер
        ser.flushOutput()       #Очищает выходной буффер
except Exception as e:
        print(e)

#Создание базы данных
try:
        DataBase()
except Exception as e:
        print(e)


#############################################
#       Функции, вызываемые командами       #
#############################################

def start(update, context):
        context.bot.send_message(chat_id = update.message.chat_id, text = "Hello! \nUse buttons below!")

def sensor_1(update, context):
        context.bot.send_message(chat_id = update.message.chat_id, text = get_value_temp(1))

def sensor_2(update, context):
        context.bot.send_message(chat_id = update.message.chat_id, text = get_value_temp(2))

def die(updater):
        updater.stop()
        exit(0)

def main():
        updater = Updater(token, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler('start', start))
        dispatcher.add_handler(CommandHandler('sensor1', sensor_1))
        dispatcher.add_handler(CommandHandler('sensor2', sensor_2))


        while True:
                try:
                        updater.start_polling()
                        tempInfo_json = ser.readline()
                        tempInfo = json.loads(tempInfo_json)
                        table_filling(tempInfo)
                except:
                        die(updater)


if __name__ == '__main__':
        main()
        

