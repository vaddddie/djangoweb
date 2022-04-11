from paho.mqtt import client as mqtt_client


broker = '192.168.4.1'
port = 1883
topic = "test/blink"
client_id = f'python-mqtt-{0}'


class connect():
    def __init__(self):
        connect.self = self

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

    def client(self):
        return client


client = connect.connect_mqtt(broker, port, topic, client_id)
client.loop_start()