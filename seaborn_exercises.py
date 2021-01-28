#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pydataset import data
import seaborn as sns


# In[ ]:





# ## Question # 1
# ### Use the iris database to answer the following quesitons:

# In[2]:


iris=sns.load_dataset('iris')
iris


# What does the distribution of petal lengths look like?

# In[3]:


sns.distplot(iris.petal_length, color= "palevioletred")
plt.title("Distribution of Petal Lengths")
plt.xlabel('Petal Length')
plt.ylabel('Distribution of Lengths')


# Is there a correlation between petal length and petal width?

# In[4]:


sns.relplot(x='petal_width', y='petal_length',hue="petal_length", data=iris)
plt.title("Petal length correlation with petal width")


# Would it be reasonable to predict species based on sepal width and sepal length?

# In[5]:


sns.relplot(x='sepal_width', y='sepal_length',hue="species",data=iris)
plt.xlabel('Sepal Width')
plt.ylabel('Sepal Length')
plt.title("Sepal Width and Sepal Height by Species")
#It would not be reasonable as the sepal length and height are too similar between setosa and versicolor


# Which features would be best used to predict species?

# In[6]:


sns.color_palette("icefire_r", as_cmap=True)
sns.relplot(x='petal_width', y='petal_length',hue="species", data=iris)
plt.xlabel("Petal Width")
plt.ylabel("Petal Length")
plt.title("petal width and petal height by species")
## It would be reasonable to use petal length and height to predict species as there is less overlap


# ## Question # 2
# ### use seaborn's load_dataset function to load the anscombe data set

# Use pandas to group the data by the dataset column, and calculate summary statistics for each dataset. <br><br>
# What do you notice?

# In[ ]:


anscombe=sns.load_dataset('anscombe')
anscombe.head(3)


# In[ ]:


anscombe.groupby('dataset').x.agg(['min', 'mean','median', 'max'])


# In[ ]:


anscombe.groupby('dataset').y.agg(['min', 'mean','median', 'max'])


# In[ ]:


anscombe.describe()


# Plot the x and y values from the anscombe data. Each dataset should be in a separate column.

# In[ ]:



sns.relplot(x="x", y="y", col="dataset", cmap='pink', data=anscombe)


# Load the InsectSprays dataset and read it's documentation. Create a boxplot that shows the effectiveness of the different insect sprays.

# In[ ]:


insect_sprays = data('InsectSprays')
insect_sprays.head()


# In[ ]:


plt.figure(figsize=(12, 10))
plt.suptitle('Boxplots of Insect Sprays')

plt.subplot(221)
sns.boxplot(data=insect_sprays, y='spray', x='count')
plt.title('Bug spray by count')

plt.subplot(222)
sns.boxplot(data=insect_sprays, y='count', x='spray')
plt.title('Count by bug spray')
plt.subplots_adjust(hspace=0.4)


# ## Question # 3
# ### Load the swiss dataset and read it's documentation. Create visualizations to answer the following questions:

# In[20]:


swiss = data('swiss')
swiss.head()


# Create an attribute named is_catholic that holds a boolean value of whether or not the province is Catholic. (Choose a cutoff point for what constitutes catholic)

# In[55]:


swiss['is_catholic'] = swiss.Catholic >50 #I decided that if more thatn 50% of people are catholic, it is fair to assume the city is catholic
swiss.head()


# Does whether or not a province is Catholic influence fertility?

# In[40]:


palette= sns.set_palette('magma_r')
sns.relplot(x='Catholic', y='Fertility', hue='is_catholic', data=swiss)


# What measure correlates most strongly with fertility?

# In[51]:


palette= sns.set_palette('mako_r')
sns.relplot(x='Agriculture', y='Fertility', data=swiss)


# In[47]:


palette= sns.set_palette('nipy_spectral_r')
sns.relplot(x='Examination', y='Fertility', data=swiss)


# In[52]:


palette= sns.set_palette('gist_earth')
sns.relplot(x='Education', y='Fertility', data=swiss)


# In[54]:


palette= sns.set_palette('icefire_r')
sns.relplot(x='Infant.Mortality', y='Fertility', data=swiss)


# ## Question # 4
# ### Using the chipotle dataset from the previous exercise, create a bar chart that shows the 4 most popular items and the revenue produced by each.

# In[8]:


from env import host, password, user
def get_db_url(db, user=user, host=host, password=password):
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'


# In[9]:


chipotle_sql_query = '''
                     SELECT *
                     FROM orders;
                     '''


# In[10]:


chipotle = pd.read_sql(chipotle_sql_query, get_db_url('chipotle'))
chipotle.head(2)


# In[11]:


chipotle.item_price = chipotle.item_price.str.replace('$', '').astype('float')
chipotle


# In[13]:


top_four= chipotle.groupby('item_name').quantity.agg('sum').nlargest(4, keep= 'all')
top_four


# In[17]:


revenue= chipotle.groupby('item_name')[['item_price']].sum().sort_values(by='item_price', ascending=False).head(4)
revenue
#This is the amount of total revenue brought in by the top 4 items


# In[85]:


top_four.plot(kind='bar',
             color='chocolate',
             width=.8)

plt.title('The Most Popular Four at Chipotle')
plt.ylabel('Number Sold')
plt.xlabel('Item Name')

plt.show()


# In[18]:


revenue.plot(kind='bar',
             color='silver',
             width=.8)

plt.title('The Most Popular Four at Chipotle')
plt.ylabel('Revenue')
plt.xlabel('Item Name')

plt.show()


# ## Question # 5
# ### Load the sleepstudy data and read it's documentation. Use seaborn to create a line chart of all the individual subject's reaction times and a more prominant line showing the average change in reaction time.

# In[28]:


sleep_study= data('sleepstudy')
sleep_study


# In[29]:


#finding the average change in reaction times
avg_change = sleep_study.groupby('Days').Reaction.agg('mean')
avg_change = avg_change.reset_index()
avg_change


# In[88]:


plt.figure(figsize=(12, 10))
plt.plot(avg_change.index, avg_change.Reaction, linewidth=8, label='Average Change', c='red', linestyle="-") #plotting the average change
plt.legend('Average Change') # adding the average change to my legend
sns.lineplot (x='Days', y='Reaction',hue='Subject',data=sleep_study, palette='seismic') # plotting each subjects reaction times over days
plt.title("Change in each subject's reaction time") #adding title to chart

