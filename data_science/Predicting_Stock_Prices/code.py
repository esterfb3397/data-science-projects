import numpy as np
import scipy
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.svm import LinearSVR
import pandas as pd





df = pd.read_csv("Predicting_Stock_Prices/AAPL.csv", sep = ',')
print(df)

# Show some summary statistics

print(df.describe())

#Prepare the data

df.set_index(pd.DatetimeIndex(df['Date']), inplace=True)

# Keep only the 'Adj Close' Value
df = df[['Adj Close']]
# Re-inspect data
print(df)

# Print Info
print(df.info())

#plt.plot(df)
#plt.show()







