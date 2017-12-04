# ---------------------------------------------------------------------------------------------
# Import
from producer.generateData import generateData
from consumer.handleData import Consumer
# ---------------------------------------------------------------------------------------------

def main():

    #consumer.
    consumer = Consumer()
    consumer.run()

main()
