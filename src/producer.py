from confluent_kafka import Producer
import json
import time
import argparse

ap = argparse.ArgumentParser(description='Data for Invoice.')
ap.add_argument("-id", "--id", required=True, type=str,
                help="id of invoice")
ap.add_argument("-total", "--grand_total", required=True, type=int,
                help="grand total of invoice")
ap.add_argument("-cus_id", "--customer_id", required=True, type=str,
                help="customer id")
args = vars(ap.parse_args())

p = Producer({'bootstrap.servers': 'localhost:9092'})


def receipt(err, msg):
    if err is not None:
        print('Error: {}'.format(err))
    else:
        print('{} : Message on topic {} on partition {} with value of {}'.format(
            time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(msg.timestamp()[1] / 1000)), msg.topic(), msg.partition(),
            msg.value().decode('utf-8')))


def create_message(id, grand_total, customer_id):
    data_dict = {'id': id, 'grand_total': grand_total, 'customer_id': customer_id}
    data = json.dumps(data_dict)
    return data


message = create_message(args['id'], args['grand_total'], args['customer_id'])

p.poll(0)
p.produce('users', message.encode('utf-8'), callback=receipt)

p.flush()
