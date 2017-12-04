if test $# -ne 2
then
     echo "Le script nécessite adresse du brocker et le topic en argument"
     return 0
fi

/usr/local/Cellar/apache-spark/2.2.0/bin/spark-submit --packages org.apache.spark:spark-streaming-kafka-0-8_2.11:2.0.2 /Users/adupeyrat/Desktop/insa/OT13/src/Application_Spark.py $1 $2