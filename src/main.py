import json
from collections import defaultdict


class Graph(object):
    def __init__(self, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed

    def add_connections(self, connections):
        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def isReachable(self, pipelines, cities, gas):
        dic = {}

        for gas_storage in gas:
            unreachable_cities = []
            for city in cities:
                if not self.bfs(city, gas_storage):
                    unreachable_cities.append(city)

            dic[gas_storage] = unreachable_cities

        print(dic)
        return dic

    def bfs(self, start, target):
        visited = {node: False for node in self.nodes()}
        queue = [start]
        visited[start] = True

        while queue:
            current_node = queue.pop(0)

            if current_node == target:
                return True

            for neighbor in self.neighbors(current_node):
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

        return False

    def nodes(self):
        return self._graph.keys()

    def neighbors(self, node):
        return self._graph[node]


pipelines = [['Львів', 'Стрий'], ['Долина', 'Львів'], ['Стрий', 'Сховище_2'], ['Долина', 'Сховище_1'],
             ['Одеса', 'Сховище_3']]

cities = ['Львів', 'Стрий', 'Долина', 'Одеса']

gas = ['Сховище_1', 'Сховище_2', 'Сховище_3']

data = {
    "pipelines": pipelines,
    "cities": cities,
    "gas": gas
}



with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)

# Зчитування даних з файлу
with open("data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

graph = Graph()
graph.add_connections(data["pipelines"])
is_reachable = graph.isReachable(data["pipelines"], data["cities"], data["gas"])

with open("result.json", "w", encoding="utf-8") as f:
    json.dump(is_reachable, f, ensure_ascii=False)
