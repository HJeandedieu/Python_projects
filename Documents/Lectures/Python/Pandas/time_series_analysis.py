import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

#Load sensor data with automatic time parsing
df = pd.read_csv("data/sensor_data_hourly.csv", parse_dates = ['timestamp'])


#Set timestamp as index for time-series operations
df = df.set_index('timestamp')

#Sort by time to ensure chronological order

df = df.sort_index()

print("First 5 rows:")
print(df.head())

print("Index info:")
print(df.index.dtype)

#Filtering for one Sensor

sensor = df[df['device_id']== 'S01'].copy()
print(f"Sensor S01 has {len(sensor)} hourly readings")

sensor['flow_rate'] = pd.to_numeric(sensor['flow_rate'], errors = 'coerce')
#RESAMPLE TO DAILY AVERAGES FOR EACH COLUMN

daily = sensor[['moisture','temperature','flow_rate']].resample("D").mean()
print("Dail averages for S01:")
print(daily.head(7))

#check the index

print("Daily index (days only):")
print(daily.index)


# VISUALIZATION PLOT

plt.figure(figsize = (10,5))
plt.plot(daily.index, daily['moisture'], marker ='o', label ='moisture', color = "green")
plt.title("Daily Average Moisture (Resampled) - S01")
plt.xlabel("Date")
plt.ylabel("Moisture(%)")
plt.xticks(rotation = 45)
plt.legend()
plt.tight_layout()
plt.show()
