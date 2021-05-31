#!/usr/bin/env python
# coding: utf-8

# In[60]:


#1
x=0
l=[1,2,3,4,5]
for i in l:
    x+=i
print('sum:',x)


# In[61]:


#2
x=1
l=[1,2,3,4]
for i in l:
    x*=i
print('Product:',x)


# In[96]:


#3
l=[5,2,1,2,1,1,3,4]
print('smallest in list',min(l))


# In[97]:


#4
l=[5,2,1,2,1,1,3,4]
print('smallest in list',max(l)) 
       


# In[8]:


#5

l=[5,2,1,2,1,1,3,4]
l.sort()
print("Second largest element in list",l[-2])




# In[20]:


#6
l=[2,66,84,101,1,104,12,8,643]
n=int(input("How many elements to print"))
l.sort()
print("Largest {} numbers are ",l[-1:n:-1])

    


# In[85]:


#7
x=[]
l=[2,66,84,101,1,104,12,8,643]
for i in l:
    if(i%2==0):
        x.append(i)
print(x)
        


# In[86]:


#8
x=[]
l=[2,66,84,101,1,104,12,8,643]
for i in l:
    if(i%2!=0):
        x.append(i)
print(x)


# In[87]:


#9
l=[2,4,'sher',[],[64,'tree']]
for i in l:
    if(type(i)==list):
        if(len(i)==0):
            l.remove(i)
print(l)


# In[91]:


#10
def clone(l):
    y=[]
    y.extend(l)
    return y
l=[2,'sher',93,'54tdb',12]
x=clone(l)
print('Orginal :',l)
print('clone :',x)


# In[94]:


#11
def search(c,y):
    count=0
    for i in c:
        if(i==y):
            count+=1
    return count
c=[]
for i in range(10):
    q=int(input('Enter list elements {}'.format(i)))
    c.append(q)
print(c)
y=int(input("enter element to be searched"))
w=search(c,y)
print('{} element has occured {}'.format(y,w))
    

