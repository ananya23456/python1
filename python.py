#!/usr/bin/env python
# coding: utf-8

# In[6]:


a = int(input("enter a number"))
b = int(input("enter a number"))
ch = int(input("enter your choice 1.addition\n 2.substraction\n 3.multiplication\n 4.division"))
               if(ch=1)
               addition = a+b
               print(addition)
               fi
               


# In[ ]:





# In[11]:


a = int(input("enter a number"))
b = int(input("enter a number"))
ch = int(input("enter your choice 1.addition\n 2.substraction\n 3.multiplication\n 4.division"))
if ch==1:
    addition = a+b
    print(addition)
elif ch==2:
    substraction = a-b
    print(substraction)
elif ch==3:
    multiplication = a/b
    print(multiplication)
elif ch==4:
    division = a/b
    print(division)
    else
    print("invalid choice")


# In[ ]:





# In[13]:


a = int(input("enter a number"))
b = int(input("enter a number"))
ch = int(input("enter your choice 1.addition\n 2.substraction\n 3.multiplication\n 4.division"))
if ch==1:
    addition = a+b
    print(addition)
elif ch==2:
    substraction = a-b
    print(substraction)
elif ch==3:
    multiplication = a/b
    print(multiplication)
elif ch==4:
    division = a/b
    print(division)
else:
    print("invalid choice")


# In[14]:


a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter your choice\n 1.AND\n 2.OR\n 3.NOT\n 4.<=\n 5.>=\n ==\n"))
print("AND=" a and b)


# In[27]:


a = int(input("enter a number"))
b = int(input("enter a number"))
print("AND =", a and b  == 90)
print("OR =", a ==4 or b==6)
print("<= =", a <= b)
print(">= =", a >= b)
print("equalto =", a == b)
print("notequalto =", a!=b)
print(not b)


# In[ ]:





# In[29]:


a = int(input("enter a number"))
b = int(input("enter a number"))
print("AND =", a and b  == 90)
print("OR =", a == 4 or b == 6)
print("<= =", a <= b)
print(">= =", a >= b)
print("equalto =", a == b)
print("notequalto =", a!=b)
print(not b)

a = int(input("enter a number"))
b = int(input("enter a number"))
print(a and b  == 90)
print(a == 4 or b == 6)
print(not b)
# In[38]:


dict1 = {"rollno":1,"name":"manu","age":45}
dict2 = {"place":"kozhikode","phoneno":1234567890}
dict1.updatedict2


# In[39]:


dict1 = {"rollno":1,"name":"manu","age":45}
dict2 = {"place":"kozhikode","phoneno":1234567890}
print(dict1.dict2)


# In[50]:


dict1 = {"rollno":1,"name":"manu","age":45}
dict2 = {"place":"kozhikode","phoneno":1234567890,"name":"liya"}
dict1.update(dict2)


# In[51]:


print(dict1)


# In[ ]:





# In[49]:


print(dict1)


# In[59]:


a = int(input("enter a number"))
b = int(input("enter a number"))
c = int(input("enter a number"))
if a>b and a>c:
    print("a is largest")
elif b>c and b>a:
    print("b is largest")
else:
    print("c is largest")


# In[66]:


list1=[1,2,3,4,5,6]
print(list1)
list1.append(9)
print(list1)
list1.insert(1,7)
print(list1)
list1.remove(6)
print(list1)
list1.pop(4)
print(list1)


# In[ ]:




