import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from importing_and_cleaning_data import starbucks_country_analysis
print(starbucks_country_analysis.head())
print(starbucks_country_analysis.columns)
#pd.set_option('display.max_columns', None)
#pd.set_option('display.max_rows', None)

# Scatter plot
sns.scatter(x = starbucks_country_analysis['GDP_€_percapita'], y = starbucks_country_analysis['Population'], s = starbucks_country_analysis['No_Starbucks'],
            hue = starbucks_country_analysis['Color'], alpha = 0.6)

# Scatter plot
#plt.scatter(x = starbucks_country_analysis['GDP_€_percapita'], y = starbucks_country_analysis['Population'], s = starbucks_country_analysis['No_Starbucks'],
           # c = starbucks_country_analysis['Color'], alpha = 0.6)

# Customizations
#plt.xlabel('GDP per Capita [in EUR]')
#plt.ylabel('Population')
#plt.title('Starbucks relating to GDP per capita and population')
#plt.text(35000, 4100000, 'Ireland')
#plt.text(4800, 599000000 * 2, 'China')
#plt.text(37800, 150000000 * 1.5, 'USA')
#plt.grid(True)

plt.show()








