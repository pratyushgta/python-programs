"""
This file contains methods for implementing Depth First Search Algorithm
AI-E6

Author: Pratyush Kumar (github.com/pratyushgta)
"""

visited = set()
def dfs(visited, graph, node):
    if node not in visited:
        print(node, end=" ")
        visited.add(node)
        for neighbors in graph[node]:
            dfs(visited, graph, neighbors)


graph = {}
n = int(input("Enter number of nodes: "))
print("\n>>> INPUT NODES & THEIR NEIGHBORS <<<")
for i in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors: ").split()
    graph[node] = neighbors

start_node = input("\nEnter the starting node: ")
print("\nFollowing is the DFS:")
dfs(visited, graph, start_node)
