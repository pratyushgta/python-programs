"""
This file contains methods for implementing Breadth First Search Algorithm
AI-E5

Author: Pratyush Kumar (github.com/pratyushgta)
"""

# graph = {
#    '5': ['3', '7'],
#    '3': ['2', '4'],
#    '7': ['8'],
#    '2': [],
#    '4': ['8'],
#    '8': []
# }

visited = []
queue = []

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbor in graph[m]:
            if neighbor not in visited:
                visited.append(neighbor)
                queue.append(neighbor)

graph = {}
n = int(input("Enter number of nodes: "))
print("\n>>> INPUT NODES & THEIR NEIGHBORS <<<")
for i in range(n):
    node = input("Enter node: ")
    neighbors = input("Enter neighbors: ").split()
    graph[node] = neighbors

start_node = input("\nEnter the starting node: ")
print("\nFollowing is the BFS:")
bfs(visited, graph, start_node)
