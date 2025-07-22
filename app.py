import pandas as pd
import numpy as np
from prophet import Prophet
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

data = pd.read_csv('sales_data.csv')
data['date'] = pd.to_datetime(data['date'])
data = data.merge(pd.read_json('weather_api.json'), on='date')
data['log_temp'] = np.log(data['temperature'] + 1)
train, test = train_test_split(data, test_size=0.2, shuffle=False)
model = Prophet(yearly_seasonality=True)
model.add_regressor('log_temp')
model.fit(train.rename(columns={'date': 'ds', 'sales': 'y'}))
forecast = model.predict(test.rename(columns={'date': 'ds'}))
mae = mean_absolute_error(test['sales'], forecast['yhat'])