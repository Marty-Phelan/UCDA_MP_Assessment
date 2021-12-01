import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from importing_and_cleaning_data import starbucks_country_analysis
print(starbucks_country_analysis.head())
print(starbucks_country_analysis.columns)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

# Scatter plot
sns.relplot(x = starbucks_country_analysis['GDP_€_percapita'], y = starbucks_country_analysis['Population'], s = starbucks_country_analysis['No_Starbucks'],
            hue = starbucks_country_analysis['Region'], kind= 'scatter', alpha = 0.6)

plt.show()








