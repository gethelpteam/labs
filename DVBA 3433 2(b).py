#!/usr/bin/env python
# coding: utf-8

# In[10]:


import numpy as np
dataset =np.genfromtxt('E:/3433/dvba/dataset.csv',delimiter=',')
print(dataset)


# In[11]:


print("The rows & columns on dataset:", dataset.shape)


# In[5]:


print("---------Perform Indexing operation on Dataset------ ")


# In[12]:


print(dataset[0])


# In[13]:


print(dataset[-1])


# In[15]:


print(dataset[1,1])


# In[16]:


print(dataset[8,3])


# In[17]:


print(dataset[[0,7,3,9],[1,-1,2,3]])


# In[18]:


print(dataset[0,3]+dataset[2,-1])


# In[19]:


print(dataset[dataset>70])


# In[20]:


print("---Perform slicing operations on dataset---")


# In[21]:


print(dataset[1:3])


# In[22]:


print(dataset[:2,:2])


# In[26]:


print(dataset[-1,::-1])


# In[27]:


print(dataset[-5:-1,:6:2])


# In[28]:


print("---perform splitting operations on dataset---")


# In[29]:


print("---Horizontal splitting---")


# In[31]:


print(np.hsplit(dataset,2))


# In[32]:


print("---vertical splitting---")


# In[33]:


print(np.vsplit(dataset,2))


# In[34]:


print("---perform Iterating operation on dataset---")


# In[35]:


print("---using nditer()---")


# In[36]:


for x in np.nditer(dataset):
    print(x)


# In[37]:


print("---using ndenumerate()---")


# In[38]:


for idx,x in np.ndenumerate(dataset):
    print(idx,x)


# In[ ]:




