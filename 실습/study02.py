#!/usr/bin/env python
# coding: utf-8

# In[2]:


score=int(input('점수를 입력하세요 '))

if score>90:
    print('10000원')
    
elif score>80:
    print('5000원')
    
else:
    print()


# In[1]:


score=int(input('점수를 입력하세요 '))

if score>=90 and score<=100:
    print('A')
    
elif score>=80 and score<90:
    print('B')

elif score>=70 and score<80:
    print('C')
    
elif score>=60 and score<70:
    print('D')

else:
    print('F')


# In[3]:


year=int(input(''))

if year%4==0:
    
    if year%400==0:
        print('1')
    elif year%100==0 and year%400!=0:
        print('0')
    else:
        print('1')
else:
    print('0')


# In[4]:


for i in range(3):
    print(i)


# In[5]:


i=0
while i<3:
    print(i)
    i=i+1


# In[6]:


for i in range(1,11):
    print(i)


# In[7]:


i=int(input('i: '))

while i!=5:
    print(i)
    i=int(input('i: '))


# In[8]:


for i in range(1,10):
    if i%2==0:
        continue
        
    print(i)


# In[10]:


n=int(input('N:'))
i=1
while i<10:
    print(n,'x',i,'=',n*i)
    i=i+1


# In[11]:


n=int(input('N:'))

for i in range(n):
    for j in range(i+1):
        print('*',end='')
    print()


# In[12]:


n=int(input('N:'))

for i in range(n):
    print(i+1)


# In[ ]:





# In[17]:


n=int(input('N:'))
s=0
for i in range(n):
    j=int(input())
    s=s+i
print(s)
        
    

