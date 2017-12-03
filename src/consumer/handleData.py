# ---------------------------------------------------------------------------------------------
# Import
from util.Constant import ServerConfig
from util.Constant import Kafka
from kafka import KafkaConsumer
import json

import logging
logging.basicConfig(level='INFO')

# ---------------------------------------------------------------------------------------------
# Code

class Consumer():
    def __init__(self):
        self.consumer = KafkaConsumer(Kafka.TOPIC_NAME,
                                      bootstrap_servers=ServerConfig.SERVER_ADRESS_CONSUMER,
                                      group_id=None,
                                      auto_offset_reset='smallest',
                                      value_deserializer=lambda m: json.loads(m.decode('ascii')))

    def stop_consumer(self):
        self.consumer.close()

    def run(self):
        print("Begin Read Message")

        for msg in self.consumer:
            print( "READ MESSAGE : " +str(msg))


