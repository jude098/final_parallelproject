import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")


import pandas as pd

def pretty_print(name, to_print):
    print(f'{name}:')
    print(f'{to_print}\n\n')

# Computing data
data = pd.read_csv(filepath_or_buffer='/users/j..l/downloads/world-happiness-report-2019.csv',
                      sep=',',
                      header=0)
#print data columns
data.columns = ['Country (region)', 'Ladder', 'SD of Ladder', 'Positive affect', 'Negative affect', 'Social support', 'Freedom', 'Corruption', 'Generosity', 'Log of GDP per capita', 'Healthy_life_expectancy']

#print data head
data.head()

#print(data.columns)

print(data)

#Structuring dataset with all columns
pretty_print("data dataframe", data.to_string())
pretty_print("data columns", data.columns)

#Getting the dataset info

data.info()

#Visualizing the correlation in the dataset

#scatterplot 2 variables

plt.scatter(data['Ladder'],data.Healthy_life_expectancy)
plt.title('Ladder compare with Healthy_life_expectancy')
plt.xlabel('Ladder')
plt.ylabel('Healthy_life_expectancy')
plt.show()

#as we can see, both variables are dependent, the more ladder will increase (ladder = measure of life satisfaction)
#the more the life expectancy will increase, as well

#heatmap
#seeing the variables displayed
#the darker the square, the stronger the relationship between the two variables is

# get correlation matrix
corr = data.corr()
fig, ax = plt.subplots()

# create heatmap
im = ax.imshow(corr.values)

# set labels
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns)
ax.set_yticklabels(corr.columns)

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=45, ha="right",
         rotation_mode="anchor")

plt.show()

# boxplots
#here we notice that there's a positive correlation between both variables and when the social support increase
#the positive affect (ie which is the measure of positive emotions increase as well)

sns.boxplot('Positive affect', 'Social support', data=data)

plt.show()

