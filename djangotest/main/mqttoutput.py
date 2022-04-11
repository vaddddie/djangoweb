import __init__


class blink:
    def blinkOn():
        client = __init__.client()
        client.publish(topic, 1)