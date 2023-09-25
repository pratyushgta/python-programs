graph = dict()
n = int(input("Enter Number of Elements:"))
for i in range(n):
    data = input("enter key separated by ':', ").split()
    temp = data.split(':')
    graph[temp[0]] = temp[1]
print()

'''graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]
}'''
visited = []
queue = []


def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)


bfs(visited, graph, '5')