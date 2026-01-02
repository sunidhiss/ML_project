import pandas as pd
import matplotlib.pyplot as plt

# Load the sub-division rainfall dataset
df = pd.read_excel("Sub_Division_rainfall.xlsx")

# Select only monsoon months
monsoon_months = ["JUN", "JUL", "AUG", "SEP"]

# Calculate average rainfall for each monsoon month
monsoon_avg = df[monsoon_months].mean()

# Plot the monsoon rainfall pattern
plt.figure()
plt.bar(monsoon_avg.index, monsoon_avg.values)
plt.xlabel("Month")
plt.ylabel("Average Rainfall (mm)")
plt.title("Average Monsoon Rainfall Pattern in India (2000–2017)")
plt.show()
