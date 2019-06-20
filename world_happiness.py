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

# Question: Can we predict the level of happiness based on the social support level using machine learning?

#data definition
df = pd.read_csv(filepath_or_buffer='/users/judelangevin/downloads/world-happiness-report-2019.csv',
                      sep=',',
                      header=0)

print(df.columns)

#results:
#Index(['Country (region)', 'Ladder', 'SD of Ladder', 'Positive affect',
 #      'Negative affect', 'Social support', 'Freedom', 'Corruption',
  #     'Generosity', 'Log of GDP\nper capita', 'Healthy life\nexpectancy'],
   #   dtype='object')

#First checking the correlation between the two values
#print('Correlation between Corruption and Negative affect:',df['Corruption'].corr(df['Negative affect']))

#result: The correlation between both variables are: 0.1589028628371875, which is not high, therefore changing the question
#wouldn't be a bad idea

#First checking the correlation between the two values
#print('Correlation between Ladder and Social support:',df['Ladder'].corr(df['Social support']))
#result: 0.8178424489505299

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#training the model with different features

features = ['Positive affect','Freedom','Log of GDP\nper capita','Social support']
temp_dataframe = df[features]
temp_dataframe = temp_dataframe.sort_values('Social support')

#temp_dataframe

del temp_dataframe['Social support']
X = temp_dataframe

# Label for Regression model Training
label = 'Ladder'
y = df[label]

from sklearn.model_selection import train_test_split

regressor = LinearRegression()
model = regressor.fit(X,y)
print(model)

#kept havving this error: ValueError: Input contains NaN, infinity or a value too large for dtype('float64')

np.where(df.values >= np.finfo(np.float64).max)
