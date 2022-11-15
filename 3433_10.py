#!/usr/bin/env python
# coding: utf-8

# In[1]:


import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data = pd.DataFrame({'Name': ['Avery Bradley', 'Jae Crowder', 'John Holland',   'R.J. Hunter', 'Jonas Jerebko', 'Amir Johnson', 
                       'Jordan Mickey', 'Kelly Olynyk','Terry Rozier','Marcus Smart'],
                   'Team': ['A','B','C','D','E','F','G','H','I','J'],
                  'Number':[12,34,12,56,67,56,78,34,67,45],
                   'Position':['PG','SG','SG','SG','PF','PF','PF','PG','PG','PG'],
                   'Age':[25,25,27,22,29,29,21,25,22,22],
                   'salary':[2500,4545,2323,2324,1456,2324,6754,3421,890,5698]
                  
                  })
print(data)


# In[2]:


#histogram
sns.histplot(data = data, x = "Number", kde = True, hue = "Position", palette="Greens")
sns.set_style("dark",{'axes.axisbelow':False,'axes.grid':True,'grid.color':'red'})
sns.set_context("notebook",font_scale=1,rc={'figure.figsize':(8,5)}) 

plt.title("Histogram plot in Seaborn",color="blue",fontsize=20)
p=sns.color_palette("deep")#deep,colorblind,dark,pastel,bright
sns.palplot(p)
plt.show()


# In[3]:


#boxplot
sns.barplot(x="Team", y="Number", data=data, hue="Position", palette="bright")
sns.set_style("dark",{'axes.axisbelow':False,'axes.grid':True,'grid.color':'red'})
sns.set_context("notebook",font_scale=1,rc={'figure.figsize':(8,5)}) 
plt.title("Bar plot in Seaborn",color="blue",fontsize=20)
p=sns.color_palette("deep")#deep,colorblind,dark,pastel,bright
sns.palplot(p)
plt.show()


# In[ ]:




