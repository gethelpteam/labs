#!/usr/bin/env python
# coding: utf-8

# In[5]:


#line plot
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("9.csv")
print(data)


# In[13]:


sns.lineplot(x="Team", y="Number", data=data, hue="Position", palette="bright")
sns.set_style("dark",{'axes.axisbelow':False,'axes.grid':True,'grid.color':'red'})
sns.set_context("notebook",font_scale=1,rc={'figure.figsize':(8,5)}) 
plt.title("Line plot in Seaborn",color="blue",fontsize=20)
p=sns.color_palette("deep")
sns.palplot(p)
plt.show()


# In[14]:


#Scatter plot
sns.scatterplot(x="Team", y="Number", data=data, hue="Position", palette="bright")
sns.set_style("dark",{'axes.axisbelow':False,'axes.grid':True,'grid.color':'red'})
sns.set_context("notebook",font_scale=1,rc={'figure.figsize':(8,5)}) 
plt.title("Scatter plot in Seaborn",color="blue",fontsize=20)
p=sns.color_palette("deep")
sns.palplot(p)
plt.show()


# In[ ]:




