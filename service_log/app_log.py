from kafka import KafkaConsumer
import logging


consumer = KafkaConsumer('sanic',
                         group_id='sanic-group',
                         bootstrap_servers=['0.0.0.0:9092'])


logging.basicConfig(filename="sanic.log", level=logging.INFO,
                    format='%(asctime)s %(name)-5s: %(levelname)s %(message)s')

for message in consumer:
    message.value.decode('utf-8')
    logging.info("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
    print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.key,
                                          message.value))
