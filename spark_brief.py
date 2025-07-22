from pyspark.sql import SparkSession
from pyspark.sql.functions import col, avg, count

spark = SparkSession.builder.appName("HRETL").getOrCreate()
df = spark.read.parquet('s3://hr_data.parquet')
df = df.filter(col('hire_date') > '2022-01-01').repartition('department')
aggregated = df.groupBy('employee_id').agg(avg('salary').alias('avg_salary'), count('*').alias('record_count'))
aggregated = aggregated.filter(col('record_count') > 100)
aggregated.write.mode('overwrite').parquet('s3://processed_hr/')