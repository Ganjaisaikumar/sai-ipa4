#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv("C:\\Users\\sai\\Downloads\\data (1).csv")
df.describe()


# In[2]:


df.isnull().sum()


# In[3]:


df.fillna(df.mean(), inplace=True)


# In[4]:


df[['Duration', 'Calories']].agg(['min', 'max', 'count', 'mean'])


# In[16]:


df_filtered = df[(df['Calories'] >= 500) & (df['Calories'] <= 1000)]
print(df_filtered)


# In[17]:


df_filtered = df[(df['Calories'] > 500) & (df['Pulse'] < 100)]
print(df_filtered)


# In[8]:


df_modified = df.drop('Maxpulse', axis=1)


# In[9]:


df['Calories'] = df['Calories'].astype(int)


# In[10]:


import matplotlib.pyplot as plt
plt.scatter(df['Duration'], df['Calories'])
plt.xlabel('Duration')
plt.ylabel('Calories')
plt.show()


# In[18]:


import pandas as pd

dataset = pd.read_csv("C:\\Users\\sai\\Downloads\\Salary_Data.csv")
dataset.head()


# In[12]:


from sklearn.model_selection import train_test_split

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 1/3, random_state = 0)


# In[19]:


from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
y_pred


# In[14]:


from sklearn.metrics import mean_squared_error

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error is :", mse)


# In[15]:


import matplotlib.pyplot as plt

plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()

plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()


# In[ ]:




