#!/usr/bin/env python
# coding: utf-8

# In[1]:


h = [x*2 for x in range(1,11)]
h


# In[13]:


h=[]
# for i in "human":
#     h.append(i)

h=[letter for letter in "human"]
h


# In[ ]:





# In[4]:


h=[x for x in range(1,21) if x%2 == 0]

h=[]
for x in range(1,21):
    if x%2==0:
        h.append(x)
h

 


# In[ ]:





# In[5]:


matrix =[[1,2,3,4],[5,6,7,8]]
transpose=[]
for i in range(len(matrix[0])):
    row=[]
    for j in matrix:
        row.append(j[i])
        transpose.append(row)
transpose    
    


# In[11]:



transpose=[[row[i] for row in matrix] for i in range(len(martrix[0]))]
transpose


# In[12]:


for i in range(10):
    if i%2==0:
        print(i)


# In[7]:


for i in range(1,10,2):
    print(i)


# In[15]:


a={'ali':"12345678",'mufadal':"987654321"}


# In[16]:


a=dict([(1,'a'),(2,'b'),(3,'c')])
a


# In[23]:


a={
    'a':["apple","bnanas","orange"],
    'b':["lemon","onion","potato"],
    'c':"car",
    'd':"bike"
    
}
# a['d']
a.get('a')[0]
a.get('f',"not found")


# In[24]:


for i in a.keys():
    print(i)


# In[25]:


for i in a.values():
    print(i)


# In[26]:


for key, value in a.items():
    print(key,value)


# In[31]:


list1 =[1,2,3,4,5,6,7] #keys
list2=['a','b','c','d','e','f','g']
res={}

# for key in list1:
#     for value in list2:
#         res[key]= value
#         list2.remove(value)
#         break

res = dict(zip(list1,list2))
res


# In[5]:


a=3*1**3
a


# In[13]:


i = 1

while True:

    if i%3 == 0:

        break

    print(i)
    i += 1


# In[18]:


i = 0

while i < 5:

    print(i)

    i += 1

    if i == 3:

        break

else:

    print(0)


# In[ ]:


x = "abcdef"

i = "a"

while i in x:

    print(i, end = " ")
    break


# In[ ]:


example = "helle"
example.find("e")
print(example)


# In[ ]:


d = {"john":40, "peter":45}
print(d)


# In[ ]:


d = {"john":40, "peter":45}
d.(john)


# In[ ]:


d1 = {"john":40, "peter":45}
d2 = {"john":466, "peter":45}
d1 == d2


# In[ ]:


a={i: 'A' + str(i) for i in range(5)}
a


# In[8]:


a={
    'a':["apple","bnanas","orange"],
    'b':["lemon","onion","potato"],
    'c':"car",
    'd':"bike"
    
}
a['a'][0]


# In[15]:


lst1=[1,2,3,4,5,6,7]
list2=['a','b','c','d','e','f','g']
res=dict(zip(lst1,list2))
res


# In[16]:


h=[x*2 for x in range(1,11)]
for i in range(len(h)):
    print(str(2) +"x"+str(i+1)+"="+str(h[i]))


# In[ ]:




