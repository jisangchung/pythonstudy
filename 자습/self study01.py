#!/usr/bin/env python
# coding: utf-8

# In[ ]:


x=int(input('x: '))
y=int(input('y: '))

if x>5:
    if y<3:
        print(x+y)
    
    elif y>=3:
         print(x-y)
if x<5:
    if y<3:
        print(x*y)
        
    elif y>=3:
        print(x/y)
        
else:
    print(x,y)
    

