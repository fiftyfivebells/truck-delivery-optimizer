import csv
from ChainedHashTable import HashTable
from Graph import Graph
from Package import Package
from Location import Location


# Takes the csv of distances from each spot to all the other spots and turns
# it into a list of each location and its distance to all the other locations
# Returns the list of distances
#
# O(n) complexity
def create_distance_list(file):
    distances = []

    with open(file, newline = '') as distances_list:
        reader = csv.reader(distances_list)

        for row in reader:
            row_data = list(map(lambda x: float(x.strip()), list(row)))
            distances.append(row_data)

    return distances


# Takes in a csv of location information and then creates a hash table where
# the name of the place is the key and a location object corresponding to the
# location in the table is the value. Returns the hash table.
#
# O(n) complexity
def create_locations_table(file):
    locations = HashTable()

    with open(file, newline = '') as locations_file:
        reader = csv.reader(locations_file)

        idx = 0

        for row in reader:
            name = row[0].strip()
            street = row[1].strip()
            city = row[2].strip()
            state = row[3].strip()
            zip_code = row[4].strip()

            l = Location(name, street, city, state, zip_code, idx)
            locations.insert(street, l)
            
            idx += 1

    return locations
    

# Takes a csv of packages and their associated data and creates a list of
# package objects. Returns the list of package objects.
#
# O(n) complexity
def create_packages_list(file):
    packages = HashTable()
    locations = create_locations_table('./files/locations.csv')
    hub = 0
    graph = create_location_graph()

    with open(file, newline='', encoding='utf-8-sig') as packages_file:
        reader = csv.reader(packages_file)

        for row in reader:
            p_id = int(row[0].strip())
            street = row[1].strip()
            weight = row[6].strip()
            deadline = row[5].strip()

            if deadline == 'EOD':
                deadline = ''
            else:
                dl = deadline.split(' ')
                deadline = dl[0] + ':00'

            address = locations[street]

            p = Package(p_id, address, deadline, weight)
            addr_idx = locations[street].graph_index
            shortest_path_to_hub = graph.shortest_paths(addr_idx)[0]
            p.distance_from_hub = shortest_path_to_hub

            packages.insert(p_id, p)

    return packages


# Creates a graph using the distances in the given CSV file. Iterates the full
# length of the row for each row in the CSV.
#
# O(n^2) complexity
def create_location_graph():
    distances = create_distance_list('./files/location_distances.csv')
    graph = Graph(len(distances))

    for i in range(len(distances)):
        for j in range(len(distances)):
            graph.add_edge(i, j, distances[i][j])

    return graph

