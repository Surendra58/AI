#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Problem statement link:
# https://1drv.ms/w/s!Am4CWHrkxn5CfLSc1UtZMCagrJs?e=GONAze


# In[22]:


import pandas as pd,numpy as np
from pandas.api.types import is_numeric_dtype
np.random.seed(42)
name=['name'+str(i) for i in range(50)]
address=['address'+str(i) for i in range(50)]
age=np.random.randint(20,100,50)
salary=np.random.randint(50000,1000000,50)
df=pd.DataFrame(data={'age':age,'name':name,'address':address,'salary':salary})
# df
def remove_outlier(df):
    low=.05
    high=.95
    quant_df=df.quantile([low,high])
    for name in list(df.columns):
      if is_numeric_dtype(df[name]):
       df=df[(df[name] > quant_df.loc[low,name]) 
               & (df[name] < quant_df.loc[high,name])]
    return df
remove_outlier(df).head()


# In[43]:


import pandas as pd
df=pd.DataFrame({'NAME':['A','B','C','D','E'],
   'Date1':['2020-04-04',
           '2020-03-04',
           '2020-08-04',
           '2020-06-04',
           '2020-05-03'],
    'Sex':['M','F','M','F','M'],
    'Date2':['2019-05-04',
           '2019-04-04',
           '2019-04-04',
           '2019-02-04',
           '2019-07-03'],
   'Date3':['2018-02-04',
           '2018-02-04',
           '2018-02-04',
           '2018-02-04',
           '2018-02-03']})
#df
mask=df.astype(str).apply(lambda x : x.str.match(r'(\d{2,4}-\d{2}-\d{2,4})+').all())
df1=df.loc[:,mask]=df.loc[:,mask].apply(pd.to_datetime)
df1


# In[69]:


# df1['Date1-Date2']=(df1['Date1'] - df1['Date2']).dt.days
Datediff1=df1['Date1'].subtract(df1['Date2']).dt.days
Datediff2=df1['Date2'].subtract(df1['Date3']).dt.days
Datediff3=df1['Date1'].subtract(df1['Date3']).dt.days
print("\nDifference of Date1 and Date2 are in Days:\n",Datediff1)
print("\nDifference of Date2 and Date3 are in Days:\n",Datediff2)
print("\nDifference of Date1 and Date3 are in Days:\n",Datediff3)
# print("Difference of Date1 and Date2 are in Days:\n", Datediff1)
# print("Difference of Date2 and Date3 are in Days:\n", Datediff2)
# print("Difference of Date1 and Date3 are in Days:\n", Datediff3)


# In[41]:


df1=pd.DataFrame({'A':[2,1,2],'C':[2,1,2]})
df2=pd.DataFrame({'A':[1,1],'B':[1,1]})
print("df1:\n",df1,"\n")
print("df2:\n",df2,"\n")
diff=get_dataframe_setdiff2d(df1,df2)
print('diff:\n','diff:\n')
#print("diff:\n","diff:"\n")
# print("diff:\n",diff,"\n")


# In[11]:


import pandas as pd,numpy as np
import random
# d=np.random.seed(4)
np.random.rand(4)


# In[15]:


import numpy as np
np.random.seed(0) 
perm=np.random.permutation(10) 
print(perm) 

