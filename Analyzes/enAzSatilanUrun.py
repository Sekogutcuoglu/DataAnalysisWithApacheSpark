from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count

# Spark session oluştur
spark = SparkSession.builder \
    .appName("LeastSoldProduct") \
    .getOrCreate()

# Kafka'dan veri okuyarak DataFrame oluştur
kafka_df = spark.read \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "your-server-ip-address:9092") \
    .option("subscribe", "your-topic-name") \
    .load()

# JSON verilerini extract et ve DataFrame'e dönüştür
json_df = kafka_df.selectExpr("CAST(value AS STRING)")

from pyspark.sql.types import StructType, StructField, StringType

schema = StructType([
    StructField("UserID", StringType(), True),
    StructField("ProductId", StringType(), True),
    StructField("ProductName", StringType(), True),
    StructField("PurchaseStatus", StringType(), True),
    StructField("Timestamp", StringType(), True),
    StructField("Ratings", StringType(), True),
    StructField("NoOfRatings", StringType(), True),
    StructField("DiscountPrice", StringType(), True),
    StructField("ActualPrice", StringType(), True),
])

df = json_df.selectExpr("from_json(value, '{}') as data".format(schema.simpleString())).select("data.*")

# Boş değerleri temizleyin
df = df.na.drop()

# Satın alma durumuna göre filtrele (PurchaseStatus == 1, yani satın alınmış ürünler)
purchased_df = df.filter(col("PurchaseStatus") == "1")

# Ürün satış sayısını hesaplayın
product_sales = purchased_df.groupBy("ProductId", "ProductName").agg(count("ProductId").alias("TotalSales"))

# En az satılan ürünü bulun
least_sold_product = product_sales.orderBy("TotalSales", ascending=True).limit(1)

# En az satılan ürünün tüm bilgilerini alın
least_sold_product_details = df.join(least_sold_product, on=["ProductId", "ProductName"], how="inner") \
    .select("UserID", "ProductId", "ProductName", "PurchaseStatus", "Timestamp", "Ratings", "NoOfRatings", "DiscountPrice", "ActualPrice")

# Sonucu gösterin
least_sold_product_details.show(truncate=False)

# Spark session'ı durdur
spark.stop()
