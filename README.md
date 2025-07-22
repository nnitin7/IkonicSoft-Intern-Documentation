IocinoSoft Sales Forecasting: Time-Series ML for Inventory Optimization






Role & Impact
As ML Intern at IocinoSoft (10/2022 - 02/2023), I led forecasting for Kowal's Market using Prophet and ARIMA in Python, integrating weather APIs to fix seasonal biases. Results: 15% accuracy improvement, 8% inventory cost reduction, 12% stockout decrease across 5+ stores. Presented insights via Tableau to ops teams.

 

Technical Workflow
Data Ingestion: SQL aggregation from store DBs.
Feature Engineering: Python with NumPy for logs/APIs.
Modeling: Prophet for seasonality, ARIMA baselines.
Validation: MAE metrics, Tableau dashboards.

Code Highlights

Python: Prophet Modeling with Weather Features
import pandas as pd
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_absolute_error

data = pd.read_csv('sales.csv')
data['date'] = pd.to_datetime(data['date'])
data = data.merge(pd.read_json('weather.json'), on='date')
data['log_temp'] = np.log(data['temperature'] + 1)
model = Prophet(yearly_seasonality=True)
model.add_regressor('log_temp')
model.fit(data.rename(columns={'date': 'ds', 'sales': 'y'}))
forecast = model.predict(data.iloc[-len(test):].rename(columns={'date': 'ds'}))
mae = mean_absolute_error(test['sales'], forecast['yhat'])

----------------------------------------------------------------------------------------------

SQL: Sales Aggregation Query
SELECT store_id, date, SUM(sales) AS total, AVG(inventory) AS avg_level
FROM sales_records
WHERE date BETWEEN '2022-10-01' AND '2023-02-01'
GROUP BY store_id, date
HAVING total > 500;

---------------------------------------------------------------------------------------------

PySpark: Distributed Feature Processing
from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate()
df = spark.read.csv('s3://sales', header=True)
df = df.groupBy('store_id', 'date').agg(sum('sales').alias('total'))
df = df.withColumn('log_total', log(col('total') + 1))
df.write.csv('s3://processed')
Demo
Run python forecast.py for modeling.
