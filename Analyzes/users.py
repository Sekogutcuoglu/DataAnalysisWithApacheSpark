from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json, desc
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType, TimestampType

# Spark Session oluşturma
spark = SparkSession.builder \
    .appName("KafkaBatchAnalysis") \
    .getOrCreate()

# Kafka'dan veri çekmek için gerekli konfigürasyonlar
kafka_bootstrap_servers = "your-server-ip-address:9092"
topic_name = "your-topic-name"

# Schema tanımlama
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
    StructField("NoOfRatings", IntegerType(), True),
    StructField("DiscountPrice", DoubleType(), True),
    StructField("ActualPrice", DoubleType(), True),
    StructField("PurchaseStatus", StringType(), True),
    StructField("Timestamp", TimestampType(), True)
])

# Kafka'dan veri okuma
df = spark.read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", kafka_bootstrap_servers) \
    .option("subscribe", topic_name) \
    .load()

# Kafka'dan gelen verileri JSON formatına dönüştürme
df = df.selectExpr("CAST(value AS STRING)")

# JSON verisini DataFrame'e dönüştürme ve gerekli alanları seçme
df = df.select(from_json(col("value"), schema).alias("data")).select("data.*")

# UserID'si birden fazla olan kayıtları listeleyen işlem
duplicate_user_ids = df.groupBy("UserID").count()

# Count'a göre en yüksekten en düşüğe sıralama
duplicate_user_ids = duplicate_user_ids.orderBy(desc("count"))

# Sonuçları gösterme
duplicate_user_ids.show(truncate=False)

# Spark Session kapatma
spark.stop()

