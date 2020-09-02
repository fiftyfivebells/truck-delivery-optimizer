
from Truck import Truck
from PriorityQueue import PriorityQueue
from WGU_Time import Time

def load_truck_from_list(truck, special, packages):
    for p in special:
        if not truck.is_truck_full():
            truck.load_truck(packages[p])
            packages[p].truck_id = truck.id
    

class WGUPS(object):
    def __init__(self, distances, locations, packages):
        self.packages = packages
        self.locations = locations

        # Set the hub location from the locations table
        hub = locations["4001 South 700 East"]

        # Make the three trucks
        self.t1 = Truck(1, distances, hub)
        self.t2 = Truck(2, distances, hub)
        self.t3 = Truck(3, distances, hub)

        # Special package rules - sorted by hand based on time or on restrictions
        # about what needs to be delivered together
        for_t1 = [13, 14, 15, 16, 19, 20, 30, 31, 34, 37, 29]
        for_t2 = [1, 3, 6, 18, 25, 28, 32, 36, 38]
        for_t3 = [9]

        # Load the reserved packages into their respective trucks
        load_truck_from_list(self.t1, for_t1, self.packages)
        load_truck_from_list(self.t2, for_t2, self.packages)
        load_truck_from_list(self.t3, for_t3, self.packages)

    # After loading the packages with special restrictions, this method takes
    # the remaining packages and puts them into a priority queue, then loads
    # then into truck 1, 2, then 3 based on distance from the hub.
    #
    # O(n) complexity
    def load_remaining_packages(self):
        package_queue = PriorityQueue()

        for k, p in self.packages:
            if p.truck_id is None:
                package_queue.enqueue(p, p.distance_from_hub)

        while (not package_queue.is_empty()):
            if not self.t1.is_truck_full():
                self.t1.load_truck(package_queue.dequeue())
            elif not self.t2.is_truck_full():
                self.t2.load_truck(package_queue.dequeue())
            else:
                self.t3.load_truck(package_queue.dequeue())        

    def run(self):
        pass
