#!/usr/bin/env python
# coding: utf-8

# In[2]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data = sns.load_dataset("fmri")
print(data)


# In[3]:


sns.boxplot(x='timepoint', y='subject', data=data, palette="Greens")
sns.set_style("dark",{'axes.axisbelow':False,'axes.grid':True,'grid.color':'red'})
sns.set_context("notebook",font_scale=1,rc={'figure.figsize':(8,5)}) 
plt.title("Box plot in Seaborn",color="blue",fontsize=20)
p=sns.color_palette("deep")#deep,colorblind,dark,pastel,bright
sns.palplot(p)
plt.show()


# In[6]:


sns.histplot(data = data, x = "timepoint", kde = True, hue = "region", palette="Greens")
sns.set_style("dark",{'axes.axisbelow':False,'axes.grid':True,'grid.color':'red'})
sns.set_context("notebook",font_scale=1,rc={'figure.figsize':(8,5)}) 
plt.title("Histogram plot in Seaborn",color="blue",fontsize=20)
p=sns.color_palette("deep")#deep,colorblind,dark,pastel,bright
sns.palplot(p)
plt.show()


# In[ ]:




