# ---------------------------------------------------------------------------------------------
# Import
import sys

from pyspark import SparkContext
#    Spark Streaming
from pyspark.streaming import StreamingContext
#    Kafka
from pyspark.streaming.kafka import KafkaUtils
#    json parsing
import json
# ---------------------------------------------------------------------------------------------

sc = SparkContext(appName="PythonSparkStreamingKafka_RM_01")
sc.setLogLevel("WARN")

def main():
    # Read parameters.
    broker, topic = sys.argv[1:]

    # Create docker stream.
    #sc = SparkContext(appName="PythonStreamingRecieverKafkaWordCount")
    ssc = StreamingContext(sc, 2)
    kafkaStream = KafkaUtils.createDirectStream(ssc, [topic], {"metadata.broker.list": broker})

    linesJson = kafkaStream.map(lambda v: json.loads(v[1]))
    text_counts = linesJson.map(lambda cashReceipt: (cashReceipt['customerID'], 1)).reduceByKey(lambda x, y: x + y)
    text_counts.pprint()

    ssc.start()
    ssc.awaitTermination()

main()