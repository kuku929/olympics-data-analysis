# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(path)
data.rename(columns={'Total':'Total_Medals'}, inplace=True)

data['Better_Event'] = np.where(data['Total_Summer'] > data['Total_Winter'], 'Summer', 'Winter')

for i in range(0, len(data)):
    if data['Total_Summer'][i] == data['Total_Winter'][i]:
        data['Better_Event'][i] = 'Both'

g = data.iloc[:-2, :]

top_countries = pd.DataFrame(g[['Country_Name','Total_Summer', 'Total_Winter','Total_Medals']])

def top_ten(df, col):
        big_list = []
        big_list.append(df.nlargest(10, col)["Country_Name"])
        return big_list

top_10_summer = top_ten(top_countries, "Total_Summer")[0]
top_10 = top_ten(top_countries, "Total_Medals")[0]
top_10_winter = top_ten(top_countries, "Total_Winter")[0]

summer_df = data[data['Country_Name'].isin(top_10_summer)]
top_df = data[data['Country_Name'].isin(top_10)]
winter_df = data[data['Country_Name'].isin(top_10_winter)]

plt.xticks(rotation=90)
plt.bar(top_df['Country_Name'],top_df['Total_Medals'])
plt.show()

summer_df['Golden_Ratio'] = g['Gold_Summer'] / g['Total_Summer'] 
winter_df['Golden_Ratio'] =  g['Gold_Winter'] / g['Total_Winter'] 
top_df['Golden_Ratio'] = g['Gold_Total'] / g['Total_Medals'] 

def top_te(df, col):
        country_list = []
        country_list.append(df.nlargest(10, col)[["Country_Name", col, "Gold_Summer"]])
        return country_list

summer_max_ratio = max(summer_df['Golden_Ratio'])
winter_max_ratio = max(winter_df['Golden_Ratio'])
top_max_ratio = max(top_df['Golden_Ratio'])

for i in range(0,10):
    if summer_df.iloc[i,-1] == summer_max_ratio:
        summer_country_gold = summer_df.iloc[i, 0]

for i in range(0,10):
    if winter_df.iloc[i,-1] == winter_max_ratio:
        winter_country_gold = winter_df.iloc[i, 0]

for i in range(0,10):
    if top_df.iloc[i,-1] == top_max_ratio:
        top_country_gold = top_df.iloc[i, 0]

g['Total_Points'] = 3*g['Gold_Total'] + 2*g['Silver_Total'] + g['Bronze_Total']

most_points = g.iloc[135,-1]
best_country = g.iloc[135,0]

best = g.loc[135,['Gold_Total','Silver_Total','Bronze_Total']]
best = pd.DataFrame({
    'Gold_Total' :  [1072],
    'Silver_Total' : [859],
    'Bronze_Total' : [750]
})

best.plot(kind='bar', stacked=True)
plt.show()

co = top_10[top_10.isin(top_10_summer)]
common = top_10_winter[top_10_winter.isin(co)]
common.dropna(inplace=True)
common.reset_index(drop=True, inplace=True)
common = np.array(common)
common

better_event = data['Better_Event'].value_counts().idxmax()









