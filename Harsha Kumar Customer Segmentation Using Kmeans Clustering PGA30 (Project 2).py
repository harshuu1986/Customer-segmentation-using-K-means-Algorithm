#!/usr/bin/env python
# coding: utf-8

# # LIBRARY IMPORT

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import seaborn as sns


# In[4]:


import matplotlib.pyplot as plt


# In[5]:


from sklearn.cluster import KMeans


# In[6]:


from matplotlib import colors


# In[7]:


from sklearn.preprocessing import StandardScaler


# # DATA IMPORT

# In[8]:


df=pd.read_csv(r"C:/Users/Asus/Downloads/customer_segmentation.csv")
df


# # DATA PREPROCESSING

# In[9]:


df.info()


# In[10]:


df=df.drop("Address",axis=1)
df


# In[11]:


df.info()


# In[12]:


df.head()


# In[13]:


df.tail()


# In[14]:


df.shape


# In[15]:


df.describe()


# In[16]:


df.columns


# In[17]:


#To find total number of unique vaules in each volumns.
df.nunique()


# In[18]:


X = df.iloc[:, [3,4]].values
X


# In[19]:


#To check null values in dataset
df.isnull().sum()


# In[20]:


#Now, once we have the count of the null values and we know the values are very less we can drop them
df = df.dropna()
print("Total missing values are:", len(df))


# In[21]:


wcss=[]


# In[22]:


for i in range(1,11):
    kmeans=KMeans(n_clusters=i, init="k-means++",random_state=42)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)


# In[23]:


plt.plot(range(1,11), wcss)
plt.title("The Elbow Method")
plt.xlabel("No Of Clusters")
plt.ylabel("WCSS Values")
plt.show()


# # TRAINING & BUILDING MODEL

# In[24]:


#Visualizing data of Years Employed and Income
plot_yearsemployed = sns.distplot(df["Years Employed"])
plot_income = sns.distplot(df["Income"])
plt.xlabel('Years Employed / Income')


# In[25]:


plt.figure(figsize=(10,6))
plt.title("Ages Frequency")
sns.axes_style("dark")
sns.violinplot(y=df["Age"])
plt.show()


# In[26]:


age18_25=df.Age[(df.Age<=25) & (df.Age>=18)]
age26_35=df.Age[(df.Age<=35) & (df.Age>=26)]
age36_45=df.Age[(df.Age<=45) & (df.Age>=36)]
age46_55=df.Age[(df.Age<=55) & (df.Age>=46)]
age55above=df.Age[df.Age>=56]

x=["18-25","26-35","36-45","46-55","55+"]
y=[len(age18_25.values),len(age26_35.values),len(age36_45.values),len(age46_55.values),len(age55above.values)]

plt.figure(figsize=(15,6))
sns.barplot(x=x , y=y , palette="rocket")
plt.title("Number Of Customer And Ages")
plt.xlabel("Age")
plt.ylabel("Number Of Customer")
plt.show()


# In[27]:


X=df.values[:,1:]
X=np.nan_to_num(X)
scaled_dataset=StandardScaler().fit_transform(X)
scaled_dataset


# In[28]:


num_clusters=3
k_means = KMeans(n_clusters=num_clusters,n_init=12)
k_means.fit(scaled_dataset)
labels=k_means.labels_
print(labels)


# In[29]:


df["labels"]=labels
df.sample(10)


# In[30]:


df.groupby("labels").mean()


# In[31]:


kmeansmodel=KMeans(n_clusters=5,init="k-means++",random_state=0)


# In[32]:


y_kmeans=kmeansmodel.fit_predict(X)


# In[33]:


plt.scatter(X[y_kmeans==0,0],X[y_kmeans==0,1],s=80,c='red',label="Customer 1")
plt.scatter(X[y_kmeans==1,0],X[y_kmeans==1,1],s=80,c='blue',label="Customer 2")
plt.scatter(X[y_kmeans==2,0],X[y_kmeans==2,1],s=80,c='yellow',label="Customer 3")
plt.scatter(X[y_kmeans==3,0],X[y_kmeans==3,1],s=80,c='black',label="Customer 4")
plt.scatter(X[y_kmeans==4,0],X[y_kmeans==4,1],s=80,c='green',label="Customer 5")
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c="magenta",label="Centroids")
plt.title("Clusters of Customers")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.legend()
plt.show()


# In[ ]:





# In[ ]:




