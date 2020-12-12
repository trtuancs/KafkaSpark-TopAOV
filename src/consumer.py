from confluent_kafka import Consumer
from load import *
from calculateAOV import *

c = Consumer({'bootstrap.servers': 'localhost:9092', 'group.id': 'python-consumer',
              'auto.offset.reset': 'earliest'})

c.subscribe(['users'])

while True:
    msg = c.poll(1.0)  # timeout
    if msg is None:
        continue
    if msg.error():
        print('Error: {}'.format(msg.error()))
        continue
    data = msg.value().decode('utf-8')
    print('Message: ', data)
    print('=============================== Top 10 AOV > 5000 ============================')
    load_data(data)
    calculate_aov()
    print('===============================================================================')

c.close()
