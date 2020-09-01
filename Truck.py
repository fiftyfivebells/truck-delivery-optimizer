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

    def load_truck(self):
        pass

    def start_deliveries(self):
        pass

    def is_truck_full(self):
        pass
