import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from importing_and_cleaning_data import starbucks_country_analysis
print(starbucks_country_analysis.head())
print(starbucks_country_analysis.columns)
# I want to create some new columns: 'Area (sq. km)', 'Pop. Density (per sq. km)', 'GDP (€ per capita)'
# Scatter plot of Starbucks per pop and GDP per capita
plt.scatter(x = starbucks_country_analysis['GDP ($ per capita)'], y = starbucks_country_analysis['Pop. Density (per sq. mi.)'], s = starbucks_country_analysis['No_Starbucks'], alpha = 0.8)
plt.show()
