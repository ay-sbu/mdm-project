import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
broker_address = 'broker.emqx.io'
port = 1883

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
        client.subscribe("ay/test")
    else:
        print("Failed to connect, return code {0}".format(rc))

def on_message(client, userdata, msg):
    print(f"Received '{msg.payload.decode()}' on topic '{msg.topic}', qos={msg.qos}")

client.on_connect = on_connect
client.on_message = on_message

try:
    client.connect(broker_address, port=port, keepalive=60)
    client.loop_forever(timeout=1)
except KeyboardInterrupt:
    print("Stopping MQTT subscriber...")
finally:
    client.disconnect()
