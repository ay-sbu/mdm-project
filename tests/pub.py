import paho.mqtt.client as mqtt
import time

# Create an instance of the MQTT client
client = mqtt.Client()

# Connect to the MQTT broker
broker_address = 'broker.emqx.io'
port = 1883
client.connect(broker_address, port=port)

# Function to publish a message
def publish_message(topic, message):
    try:
        client.publish(topic, message)
        print(f"Published message: '{message}' to topic '{topic}'")
    except Exception as e:
        print(f"Failed to publish message: {e}")

# Main function
if __name__ == "__main__":
    topic = "ay/results"
    message_count = 5
    
    print("Starting MQTT publisher. Press Ctrl+C to stop after {} messages.".format(message_count))
    
    try:
        for i in range(message_count):
            message = f"abbasssss Message {i+1}"
            publish_message(topic, message)
            time.sleep(1)  # Wait for 1 second between messages
            
    except KeyboardInterrupt:
        print("\nStopping MQTT publisher...")

    finally:
        client.disconnect()
