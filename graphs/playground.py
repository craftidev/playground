from collections import deque

# Data
airports_data = [
    'BGI', 'CDG', 'DEL', 'DOH',
    'DSM', 'EWR', 'EYW', 'HND',
    'ICN', 'JFK', 'LGA', 'LHR',
    'ORD', 'SAN', 'SFO', 'SIN',
    'TLV', 'BUD'
]

routes_data = [
    ['DSM', 'ORD'],
    ['ORD', 'BGI'],
    ['BGI', 'LGA'],
    ['SIN', 'CDG'],
    ['CDG', 'SIN'],
    ['CDG', 'BUD'],
    ['DEL', 'DOH'],
    ['DEL', 'CDG'],
    ['TLV', 'DEL'],
    ['EWR', 'HND'],
    ['HND', 'ICN'],
    ['HND', 'JFK'],
    ['ICN', 'JFK'],
    ['JFK', 'LGA'],
    ['EYW', 'LHR'],
    ['LHR', 'SFO'],
    ['SFO', 'SAN'],
    ['SFO', 'DSM'],
    ['SAN', 'EYW']
]

starting_airport = 'LGA'

# Implementation
class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, source, destination):
        # Add a unidirectionnal connection
        if source in self.graph:
            self.graph[source].append(destination)
        else:
            self.graph[source] = [destination]

    def find_routes(self, start, end, path=[]):
        # Depth-First Search
        path = path + [start]

        if start == end:
            return [path]

        if start not in self.graph:
            return []

        routes = []
        for neighbor in self.graph[start]:
            if neighbor not in path:
                new_routes = self.find_routes(neighbor, end, path)
                for new_route in new_routes:
                    routes.append(new_route)

        return routes

# Adding routes in data
necessary_routes = [
]

for route in necessary_routes:
    routes_data.append(route)

# Init graph with data
airport_graph = Graph()
for route in routes_data:
    airport_graph.add_edge(route[0], route[1])
print(airport_graph.graph)

def find_shortest_path(graph, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            for neighbor in graph.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

            visited.add(node)

    return []

# Find the minimum additional routes for all airports
for airport in airports_data:
    if airport != starting_airport:
        shortest_path = find_shortest_path(airport_graph.graph, starting_airport, airport)
        if shortest_path:
            necessary_routes.append(shortest_path)

# Display all possible routes
missing_routes = []
for airport in airports_data:
    routes = airport_graph.find_routes(starting_airport, airport)
    if routes != []:
        print('Routes for ' + starting_airport + ' to ' + airport + ':')
        for route in routes:
            print(" -> ".join(route))
    else:
        missing_routes.append(airport)

print('All routes missing:')
print(missing_routes)
print('Necessary routes:')
for route in necessary_routes:
    print(" -> ".join(route))
