import networkx as nx

# Создаем граф
G = nx.DiGraph()

# Добавляем ребра
edges = [
    ('A', 'Б'), ('A', 'В'), ('A', 'Г'), ('A', 'Д'),
    ('Б', 'В'), ('Б', 'E'),
    ('В', 'Е'), ('В', 'Ж'), ('В', 'З'), ('Г', 'В'), ('Г', 'З'),
    ('Д', 'Г'), ('Д', 'З'),
    ('Е', 'Ж'), ('Е', 'И'), ('З', 'Ж'), ('З', 'И'), ('Ж', 'И'), ('И', 'К'), ('И', 'Л'),
    ('К', 'М'), ('Л', 'М')
]
G.add_edges_from(edges)

# Удаляем вершину E
G.remove_node("Е")

# Проверяем пути из A в Л
paths_to_L = list(nx.all_simple_paths(G, source='A', target='Л'))
print("Пути из A в Л:")
print(paths_to_L)

# Проверяем пути из Л в М
paths_from_L_to_M = list(nx.all_simple_paths(G, source='Л', target='М'))
print("Пути из Л в М:")
print(paths_from_L_to_M)

# Считаем общее количество
total_paths = len(paths_to_L) * len(paths_from_L_to_M)
print("Общее количество путей из A в M через Л:", total_paths)
