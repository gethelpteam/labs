#!/usr/bin/env python
# coding: utf-8

# In[75]:


import numpy as np
print("----Indexing Operations----")
print("----Indexing on 1d----")
array1d = np.array([1,2,3,4,5,6,7,8,9])
print(array1d)
print(array1d[0])


# In[2]:


print(array1d[-1])


# In[3]:


print(array1d[3])


# In[4]:


print(array1d[-5])


# In[17]:


print(array1d[[0,2,1]])


# In[20]:


print("----Indexing on 2d----")
array2d = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array2d)


# In[21]:


print(array2d[0,0])


# In[22]:


print(array2d[0,1])


# In[23]:


print(array2d[0,2])


# In[24]:


print(array2d[2,-2])


# In[25]:


print(array2d[1,-1])


# In[26]:


print(array2d[[0,1,2],[1,0,2]])


# In[27]:


print(array2d[[0,1,2,],[-1,0,-3]])


# In[28]:


print(array2d[0,2]+array2d[1,1])


# In[30]:


print("----Indexing on 3d----")
array3d = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(array3d)


# In[31]:


print(array3d[0,1,2])


# In[32]:


print(array3d[0,-2,1])


# In[33]:


print(array3d[0,0,2])


# In[34]:


print(array3d[[0,0,0],[1,0,1],[1,0,2]])


# In[35]:


print(array3d[[0,1,0,1],[1,0,1,-1],[1,0,2,-3]])


# In[36]:


print(array3d[1,-1,2]+array3d[0,-1,-3])


# In[37]:


print("----Slicing Ōperations----")
print("----Slicing on 1d----")
print(array1d)


# In[38]:


print(array1d[4:])


# In[39]:


print(array1d[:4])


# In[40]:


print(array1d[4:7])


# In[41]:


print(array1d[:-1])


# In[42]:


print(array1d[:-2])


# In[43]:


print(array1d[::-1])


# In[44]:


print(array1d[::-2])


# In[45]:


print(array1d[-2::-2])


# In[46]:


array1d[0] = 10
print(array1d)


# In[47]:


print("----slicing on 2d----")
print(array2d)


# In[48]:


print(array2d[:,0:2])


# In[49]:


print(array2d[1:3,0:3])


# In[50]:


print(array2d[-1::-1,-1::-1])


# In[51]:


print(array2d[0:2,0:2:2])


# In[52]:


print(array2d[1,0:2:2])


# In[53]:


print("----slicing on 3d----")
print(array3d)


# In[54]:


print(array3d[0,1,2])


# In[55]:


print(array3d[1,-1,2])


# In[57]:


print(array3d[1,0:1,0:2])


# In[58]:


print(array3d[0:2,0:2,0:2])


# In[59]:


print(array3d[0:2,1,-3])


# In[61]:


print("----splitting operations----")
print("----splitting on 1d----")
print(array1d)


# In[74]:


print("----splitting on horizontally----")
np.split(array1d,3)


# In[70]:


np.split(array1d,3)


# In[68]:


np.array_split(array1d,3)


# In[76]:


print("----splitting on 2d----")
print(array2d)
print("----splitting on horizontal on 2d (column-wise)----")


# In[77]:


np.hsplit(array2d,3)


# In[78]:


np.split(array2d,3,1)


# In[79]:


np.array_split(array2d,3,1)


# In[80]:


print("----splitting on vetical on 2d(row-wise)----")
print(array2d)


# In[81]:


np.vsplit(array2d,3)


# In[82]:


np.split(array2d,3,0)


# In[83]:


np.array_split(array2d,3,0)


# In[87]:


print("----splitting on 3d----")
print(array3d)
print("----splitting on horizontal on 3d----")


# In[85]:


np.split(array3d,2)


# In[86]:


np.split(array3d,2,1)


# In[88]:


np.array_split(array3d,2,1)


# In[89]:


print("----splitting on vertical on 3d----")


# In[90]:


np.vsplit(array3d,2)


# In[91]:


np.split(array3d,2,0)


# In[92]:


np.array_split(array3d,2,0)


# In[94]:


print("----Iterating operations----")
print("----Iterating arrays using nditer()----")
print("----Iterating operations on 1d----")
print(array1d)


# In[96]:


for x in np.nditer(array1d,flags=['buffered'],op_dtypes=['S']):
    print(x)


# In[97]:


print("----Iterating operations on 2d----")
print(array2d)


# In[99]:


for x in np.nditer(array2d[:,::2]):
    print(x)


# In[100]:


print("----Iterating operations on 3d----")
print(array3d)


# In[102]:


for x in np.nditer(array3d[:,::2,2]):
    print(x)


# In[104]:


for x in np.nditer(array3d):
    x=5*x
    print(x)


# In[106]:


print("----Using ndenumerate()----")
for id,x in np.ndenumerate(array3d):
    print(id,x)


# In[ ]:




