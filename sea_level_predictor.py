import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


df = pd.read_csv('epa-sea-level.csv')

plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Observed Data', alpha=0.5)

res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
x_pred = pd.Series(range(1880, 2051))
y_pred = res.intercept + res.slope * x_pred
plt.plot(x_pred, y_pred, 'r', label='Best Fit Line (1880–2050)')

df_recent = df[df['Year'] >= 2000]
res_recent = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
x_pred_recent = pd.Series(range(2000, 2051))
y_pred_recent = res_recent.intercept + res_recent.slope * x_pred_recent
plt.plot(x_pred_recent, y_pred_recent, 'green', label='Best Fit Line (2000–2050)')

plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()
plt.grid(True)


plt.savefig('sea_level_plot.png')
plt.show()