class Graph:
    def __init__(self, vertices):
        # creates a 2d list of vertices, where each entry in the table is a
        # weighted edge between the row vertex and the column vertex
        self.graph = [[0 for col in range(vertices)]
                      for row in range(vertices)]

        # total number of vertices in graph
        self.vertices = vertices 

    # Takes in two vertices that exist in the graph and a weight. It then
    # adds an entry into spot for both vertices that represents the weighted
    # edge between them.
    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    def get_distance_between(self, u, v):
        pass

    def shortest_distance(self, start):
        pass
