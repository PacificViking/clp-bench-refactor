# executed within container
import sys

from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("spark-bench") \
    .master("spark://localhost:7077") \
    .config("spark.sql.caseSensitive", True) \
    .getOrCreate()

df = spark.read.json(sys.argv[1])
df.write.parquet(sys.argv[2], mode="overwrite", compression="zstd")  # need to set zstd(3)
