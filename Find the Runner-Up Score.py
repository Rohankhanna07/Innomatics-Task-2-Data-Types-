#!/usr/bin/env python
# coding: utf-8

# task 2
# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

# In[10]:


if __name__ == '__main__':
    n = int(input())
    array = map(int, input().split())
array=sorted(array,reverse=True)
for a in range(len(array)):
        if array[a]==array[0]:
            continue
        else:
            print(array[a])  
            break

