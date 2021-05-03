#!/usr/bin/env python
# coding: utf-8

# In[37]:


""" Breadth First Search """

import time

# Using a Python dictionary to act as an adjacency list

graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited = [] # List to keep track of visited nodes.
queue = []     #Initialize a queue

def bfs(visited, graph, node):
  visited.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print(s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited.append(neighbour)
        queue.append(neighbour)

# Driver Code(

print("Sequence:","\n")
bfs(visited, graph, 'A')
print()
print()

print("Time Taken:")
print()
print(time.process_time())
print()
print("Process finished with exit code 0")


# In[38]:


""" Depth First Search """


# Using a Python dictionary to act as an adjacency list

graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

visited = set() # Set to keep track of visited nodes.

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


# Driver Code

print("Sequence:","\n")

dfs(visited, graph, 'A')
print()
print()

print("Time Taken:")
print()
print(time.process_time())
print()
print("Process finished with exit code 0")

