from paho.mqtt import client as mqtt_client
from datetime import datetime, timezone
from .models import Cell
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
        client.subscribe(topic)  # Subscribe on the topic "heartbeat"

    def on_message(client, userdata, msg):
        def as_complex(dct):
            if '__complex__' in dct:
                return complex(dct['real'], dct['imag'])
            return dct

        # ========================= receiving a message by MQTT =========================
        j_string = json.loads(msg.payload.decode('UTF-8'), object_hook=as_complex)
        print(j_string)

        if j_string['Light'] == 1:
            light = True
        else:
            light = False

        cells = Cell.objects.all()
        for cell in cells:
            if cell.MacAddress == j_string['ID']:
                cell.Temperature = j_string['Temperature']
                cell.Humidity = j_string['Humidity']
                cell.Light = light
                cell.TimeOfTheLastMessage = datetime.now(timezone.utc)
                cell.AvailabilityOfWater = j_string['WaterS']
                cell.save()
                break
        else:
                new_esp = Cell(
                    Name=f'Farm №{len(cells) + 1}',
                    MacAddress=j_string['ID'],
                    Temperature=j_string['Temperature'],
                    Humidity=j_string['Humidity'],
                    Light=light,
                    AvailabilityOfWater=j_string['WaterS'],
                    TimeTarget=datetime.now(timezone.utc),
                    TimeLeft='None',
                    TimeOfTheLastMessage=datetime.now(timezone.utc),
                    GrowthProcess=0,
                    Online=True,
                    Mode='None'
                )
                new_esp.save()
        # ===============================================================================

    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client

# ========================= message sending function =========================
def output_msg(client, msg, topic):
    msg = json.dumps(msg)
    client.publish(topic, msg)
