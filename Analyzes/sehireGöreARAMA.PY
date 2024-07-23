from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Spark Session oluşturma
spark = SparkSession.builder \
    .appName("KafkaBatchAnalysis") \
    .getOrCreate()

# Kafka'dan veri okuma
kafka_df = spark \
    .read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "your-server-ip-address:9092") \
    .option("subscribe", "your-topic-name") \
    .load()

# JSON formatındaki verileri almak için değerlerin dizesine çevirme
value_df = kafka_df.select(col("value").cast("string").alias("value"))

# JSON verilerini DataFrame'e dönüştürme
json_df = spark.read.json(value_df.rdd.map(lambda r: r.value))

# İstanbul şehrinden yapılan alışverişlerin verilerini filtreleme
istanbul_df = json_df.filter(json_df.City == "Mardin")

# main_category'ye göre gruplama
grouped_df = istanbul_df.groupBy("MainCategory").count()

# Sonuçları gösterme
grouped_df.show()

# Spark Session'ı kapatma
spark.stop()


