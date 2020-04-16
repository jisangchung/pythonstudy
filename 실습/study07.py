#!/usr/bin/env python
# coding: utf-8

# In[5]:


line1 = input( )

n = int(line1.split()[0])
x = int(line1.split()[1])

numbers = input().split( )

answer = []

for i in numbers:
    if x>int(i):
        answer.append(i)
        
for i in answer:
    print(i, end= ' ')


# In[7]:


n = input( ) 
answer = 0

for i in range(1, int(n) + 1):
    string = str(i)
    length = len(string)
    
    if length <3:
        answer += 1
    
    else:
        d = int(string[1]) - int(string[0])
        is_num = True
        
        for j in range(2, length):
            if d !=int(string[j]) - int(string[j-1]):
                is_num = False
            
        answer += int(is_num)
        
print(answer)
        


# In[10]:


n = int(input( ))

for i in range(1, n+1):
    print(i*'*')

for j in range(1, n):
    print((n-j)*'*')


# In[6]:


n = int(input( ))

for i in range(1, n+1):
    print(' '*(i-1)+(1+2*(n-i))*'*')
    
for i in range(n - 1 , 0, -1):
    print(' '*(i-1)+(1+2*(n-i))*'*')

