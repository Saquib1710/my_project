import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
a=pd.read_csv(r"c:\Users\ASUS\Downloads\supermarket_sales.csv")

print(a.to_string())
a['Date']=pd.to_datetime(a['Date'])
a['Month'] =a['Date'].dt.month
monthly_sales=a.groupby('Month')['Price'].sum()

plt.bar( monthly_sales)
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.title("Monthly Revenue from Supermarket Sales")
plt.show()
plt.show()
