
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

    # Loads the remaining packages and then runs the deliveries for each
    # truck at the specified time. Then prints out the result and prompts
    # the user for times to show package statuses.
    #
    # O(n^2) complexity (dominated by start_deliveries from the truck class)
    def run(self):
        self.load_remaining_packages()

        # set truck 1 packages departure times
        for p in self.t1.packages:
            p.departure_time = Time("8:00:00")
        self.t1.start_deliveries("8:00:00")

        # set truck 2 package departure time
        for p in self.t2.packages:
            p.departure_time = Time("9:05:00")
        self.t2.start_deliveries("9:05:00")

        # update the address of the wrong package
        self.packages[9].address = self.locations['410 S State St']
        print(self.packages[9].address)        

        # set truck 3 packages departure times
        for p in self.t3.packages:
            p.departure_time = Time("10:20:00")
        self.t3.start_deliveries("10:20:00")

        result = round(self.t1.total_distance + self.t2.total_distance + self.t3.total_distance, 2)
        time = self.t3.current_time if self.t3.current_time > self.t2.current_time else self.t2.current_time

        print(f"\nThe total distance traveled was {result} and the ending time was {time}")

        inp = None

        while inp != 'q' and inp != 'Q':
            inp = input("\n\nEnter a time (HH:mm:ss) to check status of all packages, or 'q' to quit: ")

            try:
                print(self.print_package_info(inp))
            except ValueError:
                print("Time should be in format: HH:mm:ss")


    # Takes in a time and prints the status and information of all of the packages
    # at that current time.
    #
    # O(n)
    def print_package_info(self, time):
        time = Time(time)
        package_list = []

        for k, v in self.packages:
            package_list.append(v)

        # sorts the list in place so packages are listed in order
        package_list.sort(key = lambda x: x.package_id)

        print(f"At {time}:") 
        for p in package_list:
            s = f"package {p.package_id:>2} was "
            if time <= p.departure_time:
                s += "still at the hub"

            elif p.departure_time < time and time < p.delivery_time:
                s += "in transit"

            elif time > p.delivery_time:
                s += "delivered"

            print(s)            
