#!/usr/bin/env python
# coding: utf-8

# task 5
# Consider a list (list = []). You can perform the following commands:
# 
# insert i e: Insert integer  at position .
# print: Print the list.
# remove e: Delete the first occurrence of integer .
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.

# In[ ]:


if __name__ == '__main__':
    N = int(input())
    List=[];
    for i in range(0,N):
        cmd=input().split();
        if cmd[0] == "insert":
            List.insert(int(cmd[1]),int(cmd[2]))
        elif cmd[0] == "append":
           List.append(int(cmd[1]))
        elif cmd[0] == "pop":
            List.pop();
        elif cmd[0] == "print":
            print(List)
        elif cmd[0] == "remove":
            List.remove(int(cmd[1]))
        elif cmd[0] == "sort":
            List.sort();
        else:
            List.reverse();


# In[ ]:




