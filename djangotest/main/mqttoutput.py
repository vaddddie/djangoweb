import __init__


def blinkOn():
    client = __init__.client()
    client.publish(topic, 1)