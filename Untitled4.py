#!/usr/bin/env python
# coding: utf-8

# In[10]:


m1 = int(input("Enter marks for test1 : "))
m2 = int(input("Enter marks for test2 : "))
m3 = int(input("Enter marks for test3 : "))
if m1<=m2 and m1<=m3:
    avg=(m3+m2)/2
elif m2<=m1 and m2<=m3:
     avg=(m1+m3)/2
elif m3<=m1 and m3<=m2:
     avg=(m1+m2)/2
print("Average of best two test marks  out of three test’s marks is", avg);

 


# In[11]:


val = int(input("Enter a value : "))
str_val = str(val)
if str_val == str_val[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
    
for i in range(10):
    if str_val.count(str(i)) > 0:
        print(str(i),"appears", str_val.count(str(i)), "times");


# In[ ]:




