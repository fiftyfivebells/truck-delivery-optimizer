
from WGU_Time import Time as T
import sys

class Truck(object):
    def __init__(self, id, distances, start, avg_speed = 18, capacity = 16):
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
    #
    # O(1) complexity (amortized)
    def load_truck(self, package):
        if len(self.packages) == self.capacity:
            return False

        self.packages.append(package)
        package.truck_id = self.id
        self.location_list.add(package.address)
        return True

    # Takes in the time for the truck to start delivering, calculates the route to
    # follow, and then starts delivering the packages. Each package is marked as
    # delivered and its delivery time is updated. Once the packages list for the truck
    # is empty, it returns to the hub.
    #
    # O(n^2) complexity
    def start_deliveries(self, time):
        # update the truck's current time
        self.current_time = T(time)

        # create the truck's semi-optimal route
        self.find_shortest_route()

        print(f"Truck {self.id} left the hub at {self.current_time}")

        for i in range(1, len(self.route)):
            current_stop = self.route[i - 1]
            next_stop = self.route[i]

            distance = self.distances.get_distance_between(current_stop.graph_index, next_stop.graph_index)
            # travel time from current to next in seconds 
            travel_time = (distance / self.avg_speed) * 3600
            print(f"Truck {self.id} is traveling from {current_stop.name} to {next_stop.name}.")

            self.location = next_stop
            self.total_distance = round(self.total_distance + distance, 2)

            self.current_time.add_seconds(int(travel_time))
            delivery_time = T(str(self.current_time))

            # When the truck is at the next location, it checks all its packages to see
            # if any can be delivered here. If so, it marks them as delivered and sets
            # their delivery time to the current time
            for p in self.packages:
                if self.location == p.address:
                    p.is_delivered = True
                    p.delivery_time = delivery_time
                    print(f"Package {p.package_id} was delivered at {delivery_time}")
                    if (p.deadline != ''):
                        if (T(p.deadline) < self.current_time):
                            print(f"\t****Package was delivered but the deadline was missed****")

        print(f"Truck {self.id} traveled a total of {self.total_distance}.")
        print(f"The time is now {self.current_time}.")

    # Returns true if the truck is at capacity, false otherwise.
    #
    # O(1) complexity
    def is_truck_full(self):
        return len(self.packages) == self.capacity

    # This is the core algorithm that finds the shortest path. It is a greedy
    # algorithm that always chooses the closest neighbor
    #
    # O(n^2) complexity
    def find_shortest_route(self):
        # Initialize the route to a list with one item: the starting location of
        # the truck. Also initialize the current location with the starting location
        route = [self.start]
        current = self.start

        # This is a list of the locations that the truck needs to visit based on the
        # packages in its list. It is created from a set, so there are no duplicate
        # locations in the list.
        locs = list(self.location_list)

        # Now we begin the main loop. This loop iterates every location in the list
        # until there are no more locations to look at
        while len(locs) > 0:
            # Initialize the nearest neighbor to None and the shortest distance to
            # infinity.
            nearest = None
            shortest = sys.maxsize

            # The nearest index is the index of the current nearest location in the
            # graph that holds the distances. It is set to 0 because 0 is the index
            # of the starting location
            nearest_idx = 0

            # This is the index to keep track of which index in the graph we're in.
            # Starts at 0 and increases for each location that is visited.
            index = 0

            # Now the inner loop iterates the locations that are left, looking for
            # the closes location to our current location
            for loc in locs:
                # Get the index in the graph of the current location and the location
                # we're looking at in the list
                u = current.graph_index
                v = loc.graph_index

                # Set closest to the distance between our current location and the
                # location we're currently looking at in the list
                closest = self.distances.get_distance_between(u, v)

                # If the value for shortest is larger than the distance between the
                # two locations, shortest is updated, the nearest location is updated,
                # and the nearest index is updated
                if shortest > closest:
                    shortest = closest
                    nearest = loc
                    nearest_idx = index

                # Update the index to match the next location in the graph
                index += 1

            # After the loop, we append the nearest location to the route list and
            # remove that location from the list of locations. Then update the current
            # location to the one we just selected.
            route.append(locs.pop(nearest_idx))
            current = nearest

        # After the list is empty, append the starting location back onto the routes
        # list so the truck goes back to the start
        route.append(self.start)

        # previous = None
        # cost = 0.0
        # for stop in route:
        #     if previous is not None:
        #         cost = round(cost + self.distances.get_distance_between(previous.graph_index, stop.graph_index), 2)

        #     previous = stop

        # Set the truck's route to the optimized route so it can follow it when it
        # does the deliveries
        self.route = route
