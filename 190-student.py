#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Name : Ishan")


# In[6]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
print("Modules imported")

bmidf = pd.read_csv("bmi.csv")
print("df read")

top_5 = bmidf.head(5)
print(top_5)
name = top_5['Age']
number = top_5['BMI']


plt.xlabel("AGE")
plt.xticks(rotation='horizontal')
plt.ylabel("BMI")


label = name
value = number 
plt.bar(label, value,width=0.4, color=('green','pink','yellow'))


# In[ ]:





# In[9]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
print("Modules imported")

bpdf = pd.read_csv("blood_pressure.csv")
print("df read")

top_5 = bpdf.tail(5)
print(top_5)
name = top_5['Age']
number = top_5['BMI']


plt.xlabel("AGE")
plt.xticks(rotation='horizontal')
plt.ylabel("BMI")


label = name
value = number 
plt.bar(label, value,width=0.4, color=('red', 'blue', 'green','pink','yellow'))


# In[5]:


#Task 4
#Data is sorted in ascending order in accordance with Blood Pressure
#Find the top 5 age group where the BloodPressure value is the highest, and plot a bar graph out of it


# In[12]:


import numpy as np
import pandas as pd
print('modules imported')

insdf = pd.read_csv('insulin.csv')
print('df read')

top_1 = insdf.head(1)
print(top_1)

print("When Insulin is the highest Glucose is: " + str(top_1['Glucose']))
print("When Insulin is the highest BMI is: " + str(top_1['BMI']))


# In[ ]:


#Task 6
#Data is sorted in descending order in accordance with Insulin value
#Find out what will be the Glucose and BMI value when the Insulin is highest


# In[ ]:





# In[ ]:




