#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Line Chart
import matplotlib.pyplot as plt
x = [10,20,30,40,50]
y = [65,98,170,220,310]
plt.plot(x,y,color='r',marker='d',mec='k',mfc='w',linestyle='dashed',linewidth='2')
plt.xlabel("Overs")
plt.ylabel("Runs Scored")
plt.title("Overwise Runs Scored \n India vs England")
plt.show()


# In[8]:


#Bar chart
import matplotlib.pyplot as plt
import numpy as np
overs = ['1-10','11-20','21-30','31-40','41-50']
runs = [65,55,70,50,80]
plt.bar(overs,runs,color=['r','g','b','c','k'],width=[0.1,0.2,0.3,0.4,0.5])
plt.xlabel("Over Interval")
plt.ylabel("Runs Scored")
plt.title("Overwise Runs Scored \n India vs England")
plt.show()


# In[11]:


#pie chart
import matplotlib.pyplot as plt
import numpy as np
branches = ['CSE','IT','ECE','EEE','CSEBS']
data = [90,40,15,45,21]
fig = plt.figure(figsize=(9,10))
mycolors = ['red','green','cyan','black','pink']
plt.pie(data,labels=branches,startangle=90,explode=[0.2,0.4,0,0,0],shadow=True,colors=mycolors,autopct='%0.2f%%')
plt.title("Dept")
plt.legend(title='Dept details',loc='upper right')
plt.show()


# In[13]:


#Scatter plot
import matplotlib.pyplot as plt
import numpy as np
x = [2,2.5,3,3.5,4.5,4.7,5.0]
y = [7.5,8,8.5,9,9.5,10,10.5]
x1 = [9,8.5,9,9.5,10,10.5,12]
y1 = [3,3.5,4.7,4,4.5,5,5.2]
plt.scatter(x,y,label="low savings high income",color='g',marker='d',linewidth=4,edgecolor='k')
plt.scatter(x1,y1,label="high savings low income",color='r',marker='s',linewidth=2,edgecolor='g')
plt.xlabel("savings")
plt.ylabel("income")
plt.title("Details of income and savings")
plt.legend()
plt.show()


# In[14]:


#Histogram
import matplotlib.pyplot as plt
age = [22,32,35,45,55,14,26,19,56,44,48,33,38,28]
years  = [10,20,30,40,50,60]
plt.hist(age,years,color='magenta',histtype='bar',edgecolor='black',rwidth=0.6)
plt.xlabel=("Emp age")
plt.ylabel=("Number of EMP")
plt.title("KVS")
plt.show()


# In[17]:


#Boxplot
import matplotlib.pyplot as plt
value1=[82,76,24,40,67,62,75,78,71,32,98,89,78,67,72,82,87,66,56,52]
value2=[62,5,91,25,36,32,96,95,3,90,95,32,27,55,100,15,71,11,37,21]
value3=[23,89,12,78,72,89,25,69,68,86,19,49,15,16,16,75,65,31,25,52]
value4=[59,73,70,16,81,61,88,98,10,87,29,72,16,23,72,88,78,99,75,30]
box_plot_data=[value1,value2,value3,value4]
plt.boxplot(box_plot_data,patch_artist=True,labels=['subject1','subject2','subject3','subject4'])
plt.show()


# In[ ]:




