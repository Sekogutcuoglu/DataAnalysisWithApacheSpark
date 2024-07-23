from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_timestamp, current_timestamp, datediff

# Spark session oluştur
spark = SparkSession.builder \
    .appName("KafkaSparkBatchAnalysis") \
    .getOrCreate()

# Kafka'dan veri okuyarak DataFrame oluştur
kafka_df = spark.read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "your-server-ip-address:9092") \
    .option("subscribe", "your-topic-name") \
    .load()

# JSON verilerini extract et ve DataFrame'e dönüştür
json_df = kafka_df.selectExpr("CAST(value AS STRING)")

# JSON string'i parse et
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

schema = StructType([
    StructField("UserID", StringType(), True),
    StructField("Name", StringType(), True),
    StructField("Gender", StringType(), True),
    StructField("DOB", StringType(), True),
    StructField("Interests", StringType(), True),
    StructField("City", StringType(), True),
    StructField("Country", StringType(), True),
    StructField("ProductId", StringType(), True),
    StructField("ProductName", StringType(), True),
    StructField("MainCategory", StringType(), True),
    StructField("SubCategory", StringType(), True),
    StructField("Ratings", DoubleType(), True),
    StructField("NoOfRatings", DoubleType(), True),
    StructField("DiscountPrice", StringType(), True),
    StructField("ActualPrice", StringType(), True),
    StructField("PurchaseStatus", IntegerType(), True),
    StructField("Timestamp", StringType(), True),
])

df = json_df.selectExpr("from_json(value, '{}') as data".format(schema.simpleString())).select("data.*")

# Timestamp kolonunu datetime formatına çevir
df = df.withColumn("Timestamp", to_timestamp(col("Timestamp")))

# Mevcut zaman ile Timestamp arasındaki farkı hesapla
df = df.withColumn("DaysSinceLastPurchase", datediff(current_timestamp(), col("Timestamp")))

# Uzun süredir alışveriş yapmamış müşterileri tespit et (örneğin, 30 günden uzun süredir)
inactive_customers = df.filter(col("DaysSinceLastPurchase") > 15)

# Inaktif müşterileri göster
inactive_customers.show(truncate=False)




