# value = 65.4321
# print(f'Значение равно {value:.2f}')

import networkx as nx

# Создаем граф
G = nx.DiGraph()

# Добавляем ребра
edges = [
    ('A', 'Б'), ('A', 'В'), ('A', 'Г'), ('A', 'Д'),
    ('Б', 'Е'), ('Б', 'Ж'),
    ('В', 'Б'), ('В', 'Ж'), ('В', 'З'), ('Г', 'В'), ('Г', 'З'),
    ('Д', 'Г'), ('Д', 'З'),
    ('Е', 'Ж'), ('Е', 'И'), ('З', 'Ж'), ('З', 'И'), ('Ж', 'И')
]
G.add_edges_from(edges)


# Проверяем пути из A в Ж
paths_to_G = list(nx.all_simple_paths(G, source='A', target='Ж'))
print("Пути из A в Ж:")
print(paths_to_G)

# Проверяем пути из Ж в И
paths_from_G_to_I = list(nx.all_simple_paths(G, source='Ж', target='И'))
print("Пути из Ж в И:")
print(paths_from_G_to_I)

# Считаем общее количество
total_paths = len(paths_to_G) * len(paths_from_G_to_I)
print("Общее количество путей из A в И через Ж:", total_paths)
