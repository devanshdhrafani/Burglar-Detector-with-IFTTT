import serial #serial communication
import time
import requests #API requests

trigger='intruder_detected'        #event name
IFTTTkey='iftttkey'  #replace with ifttt maker webhook service key
url='https://maker.ifttt.com/trigger/'+trigger+'/with/key/'+IFTTTkey+'?value1=Intruder Detected!'

ser = serial.Serial('COM8', 9600, timeout=0)  #open serial communication with port COM8
 
#wait for 3s 
time.sleep(3)

while True:
    read= ser.readline().decode('utf-8') #read Arduino's Serial port and decode bytes to String
    intread=int(read[0])  #as output is number followed by \n
    print(intread)
    if intread==1:
        requests.get(url)
        break

