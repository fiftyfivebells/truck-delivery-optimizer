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
    #
    # O(1) complexity
    def add_edge(self, u, v, weight):
        self.graph[u][v] = weight
        self.graph[v][u] = weight

    # Looks into the table and finds the distance between the two given vertices
    #
    # O(1) complexity (array lookup)
    def get_distance_between(self, u, v):
        return self.graph[u][v]

    # Finds the vertex with the smallest distance value from the set of vertices
    # that are not yet included in the shortest path table
    #
    # O(n) complexity
    def __min_distance(self, distance, visited):
        min = float('inf')

        for v in range(self.vertices):
            if distance[v] < min and visited[v] == False:
                min = distance[v]
                min_index = v
                
        return min_index

    # Uses Dijkstra's algorithm to find the shortest distance between the provided
    # starting vertex and all the other vertices in the graph. Returns the list of
    # distances from the selected node to all other nodes.
    #
    # O(n^2) complexity
    def shortest_paths(self, start):
        # initialize the list of distances to a large value
        distance = [float('inf') for _ in range(self.vertices)]

        # the distance to the starting node from the starting node is always 0
        distance[start] = 0

        # initializes the table of visited vertices to False for each one, since
        # at this point none have been visited
        visited = [False for _ in range(self.vertices)]

        for _ in range(self.vertices):
            # gets the closest unvisited vertex from the starting node
            u = self.__min_distance(distance, visited)

            # sets the returned vertex as visited
            visited[u] = True

            # Looks at every vertex v in the list that has not been visited and compares
            # the distance from v to the selected vertex u plus the distance between u
            # and v. If the the distance of u plus the distance between u and v is less than
            # the distance to v, it is updated.
            for v in range(self.vertices):
                if self.graph[u][v] > 0 and visited[v] == False and distance[v] > distance[u] + self.graph[u][v]:
                    distance[v] = distance[u] + self.graph[u][v]

        return distance
