import pandas as pd
import matplotlib.pyplot as plt

# Load the sub-division rainfall dataset
df = pd.read_excel("Sub_Division_rainfall.xlsx")

# Calculate yearly average rainfall across all subdivisions
yearly_avg = df.groupby("YEAR")["ANNUAL"].mean()

# Plot year-wise rainfall trend
plt.figure()
plt.plot(yearly_avg.index, yearly_avg.values, marker='o')
plt.xlabel("Year")
plt.ylabel("Average Annual Rainfall (mm)")
plt.title("Year-wise Average Rainfall Trend in India (2000–2017)")
plt.grid(True)
plt.show()
