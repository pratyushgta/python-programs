from queue import PriorityQueue

class Graph:
    def __init__(self):
        self.graph = {}
        self.edges = {}
        self.weights = {}
        self.heuristics = {}

    def add_edge(self, from_node, to_node, weight):
        if from_node not in self.graph:
            self.graph[from_node] = []
        self.graph[from_node].append((weight, to_node))
        self.edges[from_node] = list(self.graph[from_node])

    def add_heuristic(self, node, heuristic):
        self.heuristics[node] = heuristic

    def neighbors(self, node):
        return self.edges.get(node, [])

    def get_cost(self, from_node, to_node):
        return [weight for weight, node in self.graph[from_node] if node == to_node][0]

    def get_heuristic(self, node):
        return self.heuristics.get(node, 0)

def astar(graph, start, goal):
    visited = []
    queue = PriorityQueue()
    queue.put((0, start))
    while not queue.empty():
        cost, node = queue.get()
        if node not in visited:
            visited.append(node)
            if node == goal:
                break
            for neighbor in graph.neighbors(node):
                neighbor_node = neighbor
                g = cost + graph.get_cost(node, neighbor_node)
                total_cost = g + graph.get_heuristic(neighbor_node)
                queue.put((total_cost, neighbor_node))
    return visited

def main():
    graph = Graph()

    while True:
        option = input("Choose an option:\n1. Add Edge\n2. Add Heuristic\n3. Find Shortest Path\n4. Exit\n")

        if option == "1":
            from_node = input("Enter the source node: ")
            to_node = input("Enter the destination node: ")
            weight = float(input("Enter the weight: "))
            graph.add_edge(from_node, to_node, weight)
        elif option == "2":
            node = input("Enter the node: ")
            heuristic = float(input("Enter the heuristic value: "))
            graph.add_heuristic(node, heuristic)
        elif option == "3":
            start = input("Enter the start node: ")
            goal = input("Enter the goal node: ")
            traversal = astar(graph, start, goal)
            print("Traversal:", traversal)
        elif option == "4":
            break
        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()