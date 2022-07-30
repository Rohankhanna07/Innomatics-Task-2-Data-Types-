#!/usr/bin/env python
# coding: utf-8

# task 3
# Given the names and grades for each student in a class of n students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
# 
# Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

# In[ ]:


result =[]
score = []
if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        scores = float(input())
        result+=[[name,scores]]
        score+=[scores]
    b=sorted(list(set(score)))[1] 
    for a,c in sorted(result):
        if c==b:
            print(a)


# In[ ]:




