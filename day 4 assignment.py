#!/usr/bin/env python
# coding: utf-8

# In[ ]:


lower=1042000
upper=702648265
for num in range(lower,upper+1):
    order=len(str(num))
    sum=0
    temp=num
    while temp>0:
        digit=temp%10
        sum=sum+digit**order
        temp=temp/10
        if num==sum:
         print(num)


# In[ ]:




