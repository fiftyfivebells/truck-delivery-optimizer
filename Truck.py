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

    def is_truck_full(self):
        pass
