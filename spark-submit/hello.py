from pyspark.sql import SparkSession

# Create a spark session
spark = SparkSession.builder.appName("HelloWorld").getOrCreate()

# Use sql() to write a raw SQL query
df = spark.sql("SELECT 'Hello World' as hello")

# Print the dataframe
df.show()
df.write.mode("overwrite").json("results")
