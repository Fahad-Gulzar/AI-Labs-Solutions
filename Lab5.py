class Graph:
    def init(self, size):
        self.V = size
        self.adj_list = [[] for _ in range(size)] 

    def addedge(self, v, w):
        self.adj_list[v].append(w)  # Add w to the list of v

    def BFS(self, s):
        visited = [False] * self.V  # Initialize visited list
        queue = []  # Initialize queue

        visited[s] = True  # Mark the starting node as visited
        queue.append(s)  # Enqueue the starting node

        while queue:  # While the queue is not empty
            s = queue.pop(0)  # Dequeue a vertex from the queue
            print(s, end=" ")  # Print the dequeued vertex

            # Get all adjacent vertices of the dequeued vertex
            for i in self.adj_list[s]:
                if not visited[i]:  # If the vertex has not been visited
                    visited[i] = True  # Mark it as visited
                    queue.append(i)  # Enqueue it

# Create a graph and add edges
graph = Graph(5)
graph.addedge(0, 1)
graph.addedge(0, 2)
graph.addedge(1, 2)
graph.addedge(2, 0)
graph.addedge(2, 3)
graph.addedge(3, 3)

print("BFS from index 2:")
graph.BFS(2)