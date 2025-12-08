import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt
a=pd.read_csv(r"c:\Users\ASUS\Downloads\student_csv.csv")
print (a.to_string())
print(a.describe())
print (a.corr(numeric_only=True))
#plot study vs marks graph

plt.scatter(a['StudyHours'],a['Marks'],c="red",alpha=0.5)
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.title("Study Hours vs Marks")

plt.ylim(0,100)
plt.show()
