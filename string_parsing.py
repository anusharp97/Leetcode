from collections import defaultdict, deque
import unittest
'''
input = "US:UK:Fedex:5, CA:FR:DHL:10, FR:UK:UPS:6"
function costOfPackages(input, "US", "UK) -> 5
function costOfPackages(input, "FR", "UK) -> 6
'''

def createGraph(routes: str):
    routes = routes.split(",")
    cities = set()
    graph = defaultdict(list)
    print("routes:", routes)
    for route in routes:
        route = route.split(":")
        graph[route[0].strip()].append((route[1].strip(), int(route[3])))
        cities.add(route[0].strip())
        cities.add(route[1].strip())
    return graph, cities

def costOfPackages(routes: str, start: str, end: str):
    graph, cities = createGraph(routes)
    print("graph", graph)
    print("cities", cities)
    if (start not in cities) or (end not in cities):
        print("Either of the start or end is not found in the inputs")
        return -1
    
    return getDistance(graph, start, end)

def getDistance(graph, source, destination):
    queue = deque()
    queue.append((0, source))
    seen = set()
    seen.add(source)
    while queue:
        dist, node = queue.popleft()
        if node == destination:
            return dist
        for nei, c in graph[node]:
            if nei not in seen:
                queue.append((dist + c, nei))
                seen.add(nei)
    return -1


class TestCostOfpackages(unittest.TestCase):
    def test_direct_path(self):
        input = "US:UK:Fedex:5, CA:FR:DHL:10, FR:UK:UPS:6"
        assert costOfPackages(input, "US", "UK") == 5
    
    def test_indirect_path(self):
        input = "US:UK:Fedex:5, CA:FR:DHL:10, FR:UK:UPS:6"
        assert costOfPackages(input, "CA", "UK") == 16



if __name__ == '__main__':
    routes = input("Please enter the input details\n")
    src = input("Please enter source code\n")
    dest = input("Please enter destination code\n")
    print(f"Cost to travel from {src} to {dest} is: {costOfPackages(routes, src, dest)}")

    print("Running unit tests")
    unittest.main()