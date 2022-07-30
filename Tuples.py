#!/usr/bin/env python
# coding: utf-8

# task 6
# Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

# In[ ]:


if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
t=tuple(integer_list)
print(hash(t))


# In[ ]:




