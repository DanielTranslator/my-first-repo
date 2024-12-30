import heapq

graph = {
    'A': {'B': 1},
    'B': {'A': 1, 'C': 2, "D": 2, "E": 7},
    'C': {'B': 2, 'E': 3},
    'D': {'B': 2, 'E': 4},
    'E': {'B': 7, 'C': 3, 'D': 4}
}


def dijkstra(graph, start, end):
    heap = [(0, start)]
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    visited = set()

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        if current_node in visited:
            continue

        visited.add(current_node)
        for neighbor, weight in graph[current_node].items():
            new_distance = current_distance + weight
            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(heap, (new_distance, neighbor))

    return distances[end]


shortest_path = dijkstra(graph, 'A', 'E')
print(shortest_path)