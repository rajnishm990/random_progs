import pandas as pd
import matplotlib.pyplot as plt 
from db import conn

df = pd.read_sql("SELECT * FROM metrics", conn, parse_dates=["timestamp"])
df.set_index("timestamp").plot()
plt.title("System Metrics Over Time")
plt.xlabel("Time")
plt.ylabel("Usage %")
plt.savefig("daily_report.png") 



