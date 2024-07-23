from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, TimestampType

# Define the schema for your JSON data (all fields as StringType)
schema = StructType() \
    .add("UserID", StringType()) \
    .add("Name", StringType()) \
    .add("Gender", StringType()) \
    .add("DOB", StringType()) \
    .add("Interests", StringType()) \
    .add("City", StringType()) \
    .add("Country", StringType()) \
    .add("ProductId", StringType()) \
    .add("ProductName", StringType()) \
    .add("MainCategory", StringType()) \
    .add("SubCategory", StringType()) \
    .add("Ratings", StringType()) \
    .add("NoOfRatings", StringType()) \
    .add("DiscountPrice", StringType()) \
    .add("ActualPrice", StringType()) \
    .add("PurchaseStatus", StringType()) \
    .add("Timestamp", TimestampType())

# Create a Spark session
spark = SparkSession.builder \
    .appName("KafkaStreamAnalysis") \
    .getOrCreate()

# Read from Kafka
df = spark \
    .readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "your-server-ip-address:9092") \
    .option("subscribe", "your-topic-name") \
    .load()

# Convert value column from Kafka into JSON and apply schema
df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Filter where PurchaseStatus = 0
filtered_df = df.filter(col("PurchaseStatus") == "0")

# Print the results (for demonstration)
query = filtered_df.writeStream \
    .outputMode("append") \
    .format("console") \
    .start()

query.awaitTermination()


