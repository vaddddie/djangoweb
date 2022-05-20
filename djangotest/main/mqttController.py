from paho.mqtt import client as mqtt_client
from datetime import datetime, timedelta
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
        j_string = json.loads(msg.payload.decode('UTF-8'), object_hook=as_complex)
        statuses = Status.objects.all()
        for status in statuses:
            if status.MacAddress == j_string['ID']:
                status.Temperature = j_string['Temperature']
                status.Humidity = j_string['Humidity']
                status.TimeDelta = datetime.now()
                status.AvailabilityOfWater = j_string['WaterS']
                status.save()
                break
        else:
                new_esp = Status(
                    FarmName=f'Farm №{len(statuses) + 1}',
                    MacAddress=j_string['ID'],
                    Temperature=j_string['Temperature'],
                    Humidity=j_string['Humidity'],
                    AvailabilityOfWater=j_string['WaterS'],
                    TimeTarget=datetime.now(),
                    TimeLeft='None',
                    TimeDelta=datetime.now(),
                    GrowthProcess=0,
                    CheckLine=True,
                    Mode='None'
                )
                new_esp.save()




    """        
            temp1 = status.TimeDelta.split('.')
            temp1 = str(temp1[0]).split()
            temp1 = str(temp1[len(temp1) - 1]).split(':')
            print(temp1)

            temp2 = str(datetime.now()).split('.')
            temp2 = str(temp2[0]).split()
            temp2 = str(temp2[len(temp2) - 1]).split(':')
            print(temp2)

            status.TimeDelta = datetime.now()
    """


    # Set Connecting Client ID
    client = mqtt_client.Client(client_id)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port)
    return client




def output_msg(client, msg, topic):
    msg = json.dumps(msg)
    client.publish(topic, msg)
