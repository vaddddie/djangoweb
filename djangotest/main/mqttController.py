from paho.mqtt import client as mqtt_client
#broker = '192.168.4.1'
#port = 1883
#topic = "test/blink"
#client_id = f'python-mqtt-{random.randint(0, 1000)}'
# username = 'emqx'
# password = 'public'

def connect_mqtt(broker, port, topic, client_id):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    #client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def blink(client, msg):
    client.publish(topic, msg)
client = connect_mqtt()
client.loop_start()

