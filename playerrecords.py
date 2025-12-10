import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

a=pd.read_csv(r"c:\Users\ASUS\Downloads\ipl_players.csv")
print(a.to_string())
print(a.describe())


top=a.loc[a['Runs'].idxmax()]
# a['Runs'] select the run coloumn from the database 
# idxmax finds the index nunmber of the row where the runs value is maximum
# a.loc[] is use to return all the detail of that row 
print("\nTop Scorer \n",top)
colors=np.array(['Red','Blue','k','Brown','hotpink','cyan','green','magenta','yellow','orange','purple'])
plt.bar(a['Name'],a['Runs'],color=colors)
plt.xlabel("player")
plt.ylabel("Runs")
plt.title("Runs scored by players in IPL 2023")

plt.show()