import Adafruit_DHT

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

f = open("TempDemo.txt", "w")
f.write("")
f.close()
f = open("TempDemo.txt", "a")
while True:
    humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    temperature = (temperature*1.8) + 32
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}*F  Humidity={1:0.1f}%".format(temperature, humidity))
        f.write("Temp={0:0.1f}*F  Humidity={1:0.1f}%\n".format(temperature, humidity))
    else:
        print("Failed to retrieve data from humidity sensor")

    

f.close()
