
from Truck import Truck
from PriorityQueue import PriorityQueue
from WGU_Time import Time

def load_truck_from_list(truck, special, packages):
    for p in special:
        if not truck.is_truck_full():
            truck.load_truck(packages[p])
            packages[p].truck_id = truck.id
    

class WGUPS(object):
    def __init__(self):
        pass

    def run(self):
        pass
