#Libraries and Packages needed to run this program
import asyncio
import time
import RPi.GPIO as GPIO
from azure.iot.device import Message
from azure.iot.device.aio import IoTHubDeviceClient
from gps import *

#IoT hub connection string 
CONNECTION_STRING="HostName=ElectronicsIII.azure-devices.net;DeviceId=DemoPi;SharedAccessKey=tqEJuwMv7gKQmUUKHjuNJ6B7nyhoZWH4wbM4KWSkMZg="

#Defining variables
running = True
DELAY = 2
TEMPERATURE = 20.0
HUMIDITY = 60
TRIG=21
ECHO=20
PIR_PIN = 23
PAYLOAD = '{{"distance": {distance}, "PIR": {pir}, "longitude":{longitude}, "latitude":{latitude}}}'
flag = True


def getPositionData(gps):
    nx = gpsd.next()
    
    if nx['class'] == 'TPV':
        global flag
        flag = False
        latitude = getattr(nx,'lat', "Unknown")
        longitude = getattr(nx,'lon', "Unknown")
        arry = [longitude, latitude]
        print ("Your position: lon = " + str(longitude) + ", lat = " + str(latitude))
        return arry
        
gpsd = gps(mode=WATCH_ENABLE|WATCH_NEWSTYLE)
 
async def main():

    try:
        # Create instance of the device client
        client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
 
        # Initialize GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.cleanup()
 
        # Read data using pin GPIO 21,20,23       
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        GPIO.setup(PIR_PIN, GPIO.IN)
 
        while True:
            
            try:
                if GPIO.input(PIR_PIN):
                    global flag
                    flag = True
                    while flag:
                        gpsResult = getPositionData(gpsd)
                    pir = 1
                    GPIO.output(TRIG,False)
                    print ("waiting for sensor to settle")
                    time.sleep(0.2)
                    GPIO.output(TRIG,True)
                    time.sleep(0.00001)
                    GPIO.output(TRIG,False)
                    while GPIO.input(ECHO)==0:
                       pulse_start=time.time()
                    while GPIO.input(ECHO)==1:
                        pulse_end=time.time()
                    pulse_duration=pulse_end-pulse_start
                    distance=pulse_duration*17150
                    distance=round(distance,2)
                    data = PAYLOAD.format(distance=distance, pir=pir, longitude = gpsResult[0], latitude=gpsResult[1])
                    message = Message(data)
                    print(f"Sending message: {message}")
                    await client.send_message(message)
                    
 
                print("Message successfully sent")
                await asyncio.sleep(1)
 
            except KeyboardInterrupt:
                print("Service stopped")
                GPIO.cleanup()
                break
 
    except Exception as error:
        print(error.args[0])
 

if __name__ == '__main__':
    asyncio.run(main())