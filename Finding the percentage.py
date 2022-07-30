#!/usr/bin/env python
# coding: utf-8

# task 4
# The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

# In[ ]:


if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    result = list(student_marks[query_name])    
perc = sum(result)/len(result);
print("%.2f" % perc);   


# In[ ]:




