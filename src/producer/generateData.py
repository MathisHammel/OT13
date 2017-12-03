# ---------------------------------------------------------------------------------------------
# Import
from kafka import KafkaProducer
from random import randint
from .cashReceipt import generateCashReceipt
from util.Constant import ServerConfig
from util.Constant import Kafka
import json

# ---------------------------------------------------------------------------------------------
# Time Maximum en second
TIME_MAXIMUM_BETWEEN_MESSAGE = 20
NUMBER_OF_CASH_RECEIPT = 20
STORE_ID = 20
AGENT_ID = 50
NUMBER_OF_CASH_RECEIPT = 20
CUSTOMER_ID = 1000
# ---------------------------------------------------------------------------------------------
# Code
class generateData:

    def __init__(self):
        self.stop_message = False
        self.producer = KafkaProducer(bootstrap_servers=[ServerConfig.SERVER_ADRESS_PRODUCER],
                                 value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def stop_send_message(self):
        self.stop_message = True


    def send_message(self):
        print('begin loop message')
        while not self.stop_message:

            cashReceiptId = randint(1, NUMBER_OF_CASH_RECEIPT)
            storeId = randint(1, STORE_ID)
            terminalId = randint(1, NUMBER_OF_CASH_RECEIPT)
            agentId = randint(1, AGENT_ID)
            customerId = randint(1, CUSTOMER_ID)

            cashRec = generateCashReceipt(cashReceiptId, storeId, terminalId, agentId, customerId)
            self.producer.send(Kafka.TOPIC_NAME, cashRec)
            print(cashRec)
            self.producer.flush()
