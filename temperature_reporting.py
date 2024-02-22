import time
import board
import Adafruit_DHT
import Adafruit_IO

# Set up the DHT sensor
dht = Adafruit_DHT.DHT11(board.D4)

# Set the temperature threshold (in degrees Celsius)
threshold = 27

# Set up the Adafruit IO client
# replace with your ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY
client = Adafruit_IO.Client("kajal_03", "aio_MHIg704kAAxdTGJmBjGSpbY8rQ4b")
# Set up the temperature feed
temperature_feed = client.feeds("temperature")

while True:
    # Read the temperature and humidity
    temperature = dht.temperature
    humidity = dht.humidity

    # Send the temperature to Adafruit IO
    client.send_data(temperature_feed.key, temperature)

    # Check if the temperature exceeds the threshold
    if temperature > threshold:
        print("Temperature exceeded threshold: {} degrees Celsius".format(temperature))
        # Send a notification or trigger an action using IFTTT here
    else:
        print("Temperature: {} degrees Celsius, humidity: {}%".format(temperature, humidity))

    # Wait 10 minutes before checking the temperature again
    time.sleep(600)
