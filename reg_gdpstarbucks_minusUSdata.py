import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from importing_and_cleaning_data import starbucks_country_analysis
print(starbucks_country_analysis.head())
print(starbucks_country_analysis.columns)

starbucks_country_analysis = starbucks_country_analysis.drop(labels= [0], axis=0)

sns.regplot(x = 'GDP_€_percapita', y = 'No_Starbucks', data = starbucks_country_analysis)

plt.show()