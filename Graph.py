class Graph:
    def __init__(self, vertices):
        # creates a 2d list of vertices, where each entry in the table is a
        # weighted edge between the row vertex and the column vertex
        self.graph = [[0 for col in range(vertices)]
                      for row in range(vertices)]

        # total number of vertices in graph
        self.vertices = vertices 

    def add_edge(self, u, v, weight):
        pass

    def get_distance_between(self, u, v):
        pass

    def shortest_distance(self, start):
        pass
