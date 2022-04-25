from paho.mqtt import client as mqtt_client
from .models import Status
import json

"""
broker = '192.168.4.1'
port = 1883
topic = "test/blink"
client_id = f'python-mqtt-{0}'
username = 'emqx'
password = 'public'
"""



def connect_mqtt(broker, port, topic, client_id):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)
        client.subscribe("test/heartbeat")

    def on_message(client, userdata, msg):
        def as_complex(dct):
            if '__complex__' in dct:
                return complex(dct['real'], dct['imag'])
            return dct
        print(json.loads(msg.payload.decode('UTF-8'), object_hook=as_complex))
        """
        j_string = json.loads(msg.payload.decode('UTF-8'), object_hook=as_complex)
        status = Status.objects.get(id=j_string['ID'])
        status.Temperature = j_string['Temperature']
        status.Humidity = j_string['Humidity']
        status.save()
        """


    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client




def blink(client, msg, topic):
    client.publish(topic, msg)
