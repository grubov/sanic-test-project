from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers=['0.0.0.0:9092'])
producer.send('my-topic', key=b'key', value=b'start kafka')
