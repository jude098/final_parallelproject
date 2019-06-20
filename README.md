# final_parallelproject

# cebd1160_final_project_parallel

| Name | Date |
|:-------|:---------------|
|Judith Langevin| Thursday June 20th, 2019|

-----

### Resources
Your repository should include the following:

- Python script for your analysis: world_happiness.py
- Results figure/saved file: 3 ones (heatmap, box plots and plot)
- Dockerfile for your experiment: n/a
- runtime-instructions in a file named RUNME.md

-----

## Research Question

# Question: Can we predict the level of happiness based on the social support level using machine learning?

### Abstract

It's quite interesting to see how we can plots so many variables together and see the correlation between them. Let's say 
we could observe and see if social support raise happiness (that actually reminded me of a recent controversy of a basic income for everyone), although there were more in-depth studies and real-life use case done on this, but machine learning and all analysis technics could help feed different questions a country might have regarding its citizen's happiness.

In this case, I focused on predicting the correlation between the ladder (one's life satisfaction) and social support and ended up seeing quite a bit of analysis.

### Introduction

The data (world happiness report) that we have is a report that states the level of happiness/global happiness (Ladder) of 156 countries' citizens happiness perception. The dataset columns are the Country (name of the country), Ladder (measure of life satisfaction/happiness), SD Ladder (standard deviation of the Ladder), positive affect (measure of positive emotions), negative affect (measure of negative emotions), social support (the extent to which Social support contributed to the calculation of the Happiness Score), Freedom (the extent to which Freedom contributed to the calculation of the Happiness Score), Corruption (the extent to which Perception of Corruption contributes to Happiness Score), Generosity (the extent to which Generosity contributed to the calculation of the Happiness Score), Log of GDP per capita (the extent to which GDP contributes to the calculation of the Happiness Score), Healthy life expectancy (the extent to which Life expectancy contributed to the calculation of the Happiness Score).

In this case, I focused on predicting the correlation between the ladder (one's life satisfaction) and social support and ended up seeing quite a bit of analysis.

source: https://www.kaggle.com/PromptCloudHQ/world-happiness-report-2019

### Methods

I decided to approach this problem with the same technics we saw in class, namely, uploading the data in panda dataframe (since it was a csv file), then exploring these data, showing the columns, starting to analyse the data in plots, so we can see patterns, correlations, but visualy to have a better grasp of it and then the machine learning part would be to predict an outcome based on one of the variable.

### Results

- At least 1 figure: https://github.com/jude098/final_parallelproject/blob/master/Boxplot_comparaison%20social%20support%20and%20positive%20affect.png?raw=true

- At least 1 "value" that summarizes either your data or the "performance" of your method: to be continued
#First checking the correlation between the two values
#print('Correlation between Corruption and Negative affect:',df['Corruption'].corr(df['Negative affect']))

#result: The correlation between both variables are: 0.1589028628371875, which is not high, therefore changing the question
#wouldn't be a bad idea

#First checking the correlation between the two values
#print('Correlation between Ladder and Social support:',df['Ladder'].corr(df['Social support']))
#result: 0.8178424489505299

- The Boxplot was intesresting in the sense that we could well see the correlation between the social support and positive emotions, which are dependent of one another, ie if we increase the social support, the positive emotions increase also.

- Looking at the correlation between variables was intesresting as well in the sense that we could re-direct the question, ie instead of taking machine learning to predict the correlation between Corruption and Negative affect (negative emotions), like I wanted to at first, I changed the question to see the correlation between the social support and happiness (life satisfaction/ladder)

### Discussion
Brief (no more than 1-2 paragraph) description about what you did. Include:

- interpretation of whether your method "solved" the problem
- suggested next step that could make it better.

### References
Class' notes from previous classes
source: https://www.kaggle.com/PromptCloudHQ/world-happiness-report-2019
-------
