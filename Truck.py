class Truck(object):
    def __init__(self, id, distances, start, avg_speed, capacity):
        self.id = id
        self.distances = distances
        self.start = start
        self.avg_speed = avg_speed
        self.capacity = capacity
        self.location = start
        self.route = []
        self.packages = []
        self.location_list = set()
        self.total_distance = 0.0
        self.current_time = None

    # Adds a package to the truck as long as the truck is not at capacity. Also
    # puts the package's delivery address into the set containing all the stops
    # the truck needs to make. Returns True if a package was added, False otherwise
    def load_truck(self, package):
        if len(self.packages) == self.capacity:
            return False

        self.packages.append(package)
        self.location_list.add(package.address)
        return True

    def start_deliveries(self):
        pass

    # Returns true if the truck is at capacity, false otherwise.
    def is_truck_full(self):
        return len(self.packages) == self.capacity

    def find_shortest_route(self):
        route = [self.start]
        current = self.start

        locs = list(self.location_list)

        while len(locs) > 0:
            nearest = None
            shortest = None

            nearest_idx = 0
            index = 0

            for loc in locs:
                u = current.graph_index
                v = loc.graph_index
                closest = self.distances.get_distance_between(u, v)

                if shortest == None or shortest > closest:
                    shortest = closest
                    nearest = loc
                    nearest_idx = index
                index += 1

            route.append(locs.pop(nearest_idx))
            current = nearest

        route.append(self.start)

        previous = None
        cost = 0.0
        for stop in route:
            if previous is not None:
                cost = round(cost + self.distances.get_distance_between(previous.graph_index, stop.graph_index), 2)

            previous = stop

        return (cost, route)
