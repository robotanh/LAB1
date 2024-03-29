import sys
import time
import random
from Adafruit_IO import MQTTClient
from simple_ai import image_detector

class Adafruit_MQTT:
    AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
    AIO_USERNAME = "robotanh"
    AIO_KEY = "aio_PSSM38mUkZOiLQsAZox3gtoZJp9A"

    def connected(self, client):
        print("Connected ...")
        for feed in self.AIO_FEED_IDs:
            client.subscribe(feed)

    def subscribe(self, client, userdata, mid, granted_qos):
        print("Subscribeb...")

    def disconnected(self, client):
        print("Disconnected...")
        sys.exit(1)

    def message(self, client, feed_id, payload):
        print("Received: " + payload)

    def __init__(self):
        self.client = MQTTClient(self.AIO_USERNAME, self.AIO_KEY)
        self.client.on_connect = self.connected
        self.client.on_disconnect = self.disconnected
        self.client.on_message = self.message
        self.client.on_subscribe = self.subscribe
        self.client.connect()
        self.client.loop_background()

# Initialize the counter
counter = 5

# Create an instance of Adafruit_MQTT
mqtt_instance = Adafruit_MQTT()

while True:
    counter = counter - 1
    if counter <= 0:
        print("Data is publishing.........")
        counter = 5
        temp = random.randint(10, 20)
        ai_result = image_detector()
        mqtt_instance.client.publish("cambien1", temp)
        mqtt_instance.client.publish("ai", ai_result)
        print("cambien1 = ",temp)
    time.sleep(1)