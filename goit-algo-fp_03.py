import heapq  

class Graph:
    def __init__(self):
        self.edges = {}
        self.nodes = set()

    def add_edge(self, u, v, weight):
        self.nodes.add(u)
        self.nodes.add(v)
        

        if u not in self.edges:
            self.edges[u] = []
        if v not in self.edges:
            self.edges[v] = []
            

        self.edges[u].append((v, weight))
        self.edges[v].append((u, weight))

    def dijkstra(self, start_node):
        distances = {node: float('infinity') for node in self.nodes}
        distances[start_node] = 0


        min_heap = [(0, start_node)]

        while min_heap:
            current_dist, current_node = heapq.heappop(min_heap)


            if current_dist > distances[current_node]:
                continue

            for neighbor, weight in self.edges.get(current_node, []):
                distance = current_dist + weight


                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(min_heap, (distance, neighbor))

        return distances

# Тестування
g = Graph()


g.add_edge('A', 'B', 1)
g.add_edge('A', 'C', 4)
g.add_edge('B', 'C', 2)
g.add_edge('B', 'D', 5)
g.add_edge('C', 'D', 1)
g.add_edge('D', 'E', 3) 
g.add_edge('C', 'E', 7) 

print("Граф створено (список суміжності):")
for node, neighbors in g.edges.items():
    print(f"Вершина {node}: {neighbors}")


start_vertex = 'A'
shortest_paths = g.dijkstra(start_vertex)

print(f"\nНайкоротші шляхи від вершини '{start_vertex}':")
for vertex, distance in sorted(shortest_paths.items()):
    print(f"До вершини {vertex}: відстань {distance}")