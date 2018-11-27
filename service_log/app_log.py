from kafka import KafkaConsumer
from datetime import datetime
import logging


consumer = KafkaConsumer('sanic',
                         group_id='sanic-group',
                         bootstrap_servers=['0.0.0.0:9092'])


logging.basicConfig(filename="sanic.log", level=logging.INFO)

for message in consumer:
    message.value.decode('utf-8')
    logging.info(datetime.strftime(datetime.now(), "%Y.%m.%d %H:%M:%S,%f"))
    logging.info("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
