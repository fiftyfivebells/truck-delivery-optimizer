# Stephen Bell: #001433854

from parse_data import create_location_graph, create_locations_table, create_packages_list
from Truck import Truck
from WGUPS import WGUPS


def main():
    graph = create_location_graph()
    locations = create_locations_table('./files/locations.csv')
    packages = create_packages_list('./files/packages.csv')

    app = WGUPS(graph, locations, packages)
    app.run()

if __name__ == '__main__':
    main()
