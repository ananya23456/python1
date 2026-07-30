#!/usr/bin/env python
# coding: utf-8

# In[24]:


import numpy as np
a = np.array([[2,3],[6,3]])
b = np.array([[4,9],[5,8]])
print("addition",a+b) 
print("substraction",a-b)
print("multiplication",a*b)
print("matrix multiplication",np.dot(a,b))
print("Transpose", np.transpose(a))
print("Transpose", np.transpose(b))


# In[26]:


import numpy as np
#create a sample matrix
X=np.array([[1,2,3],[4,5,6],[7,8,9]])

#perform SVD
U,S,VT=np.linalg.svd(X)

#choose the number of components to keep(eg:2)
n_components=2

#Reconstruct the matrix with reduced dimensions
X_reconstructed=np.dot(U[:,:n_components],np.dot(np.diag(S[:n_components]),VT[:n_components,:]))
print("Original matrix:")
print(X)
print("\nReconsructed Matrix(with reduced dimensions):")
print(X_reconstructed)


# In[35]:


import matplotlib.pyplot as plt
x=[2,4,6,8,10]
y=[6,3,5,4,9]
plt.plot(x,y)
plt.title("Graph")
plt.xlabel("petal length")
plt.ylabel("sepal length")


# In[41]:


import matplotlib.pyplot as plt
subjects=["english","malayalam","maths","science"]
marks=[30,40,10,18]
plt.bar(subject,marks)
plt.title("Graph")
plt.xlabel("subjects")
plt.ylabel("marks")


# In[45]:


import matplotlib.pyplot as plt
subjects=["english","malayalam","maths","science"]
marks=[30,40,10,18]
plt.scatter(subject,marks)
plt.title("Graph")
plt.xlabel("subjects")
plt.ylabel("marks")


# In[53]:


import matplotlib.pyplot as plt
subjects=["english","malayalam","maths","science"]
marks=[30,40,10,18]
plt.hist(marks)
plt.title("Graph")
plt.xlabel("subjects")
plt.ylabel("marks")


# In[54]:


import matplotlib.pyplot as plt
subjects=["english","malayalam","maths","science"]
marks=[30,40,10,18]
plt.plot(marks)
plt.legend("marks")
plt.title("Graph")
plt.xlabel("subjects")
plt.ylabel("marks")


# In[57]:


import matplotlib.pyplot as plt
subjects=["english","malayalam","maths","science"]
marks=[30,40,10,18,56,97,21,34,67,70]
plt.pie(marks)
plt.legend("marks")
plt.title("Graph")
plt.xlabel("subjects")
plt.ylabel("marks")
plt.show()


# In[60]:


import matplotlib.pyplot as plt
x=[1,2,6,18]
y=[3,10,12,20]
plt.plot(x,y,'r:o')
plt.show()


# In[ ]:




