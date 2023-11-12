from collections import deque


def BFS(graph, vis, start_node, value):
    q = deque()
    q.append(start_node)
    vis[start_node] = True
    x_component = set()

    while q:
        node = q.popleft()
        x_component.add(node)

        for neighbor in graph[node]:
            if not vis[neighbor] and neighbor in value:
                q.append(neighbor)
                vis[neighbor] = True

    return x_component


def main(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    vis = {(i, j): False for i in range(rows) for j in range(cols)}
    graph = {}  # Граф для сусідів  вузла
    change_value = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 'X':
                change_value.add((i, j))

            neighbors = []
            if i > 0:
                neighbors.append((i - 1, j))
            if j > 0:
                neighbors.append((i, j - 1))
            if i < rows - 1:
                neighbors.append((i + 1, j))
            if j < cols - 1:
                neighbors.append((i, j + 1))

            graph[(i, j)] = neighbors

    for value in change_value:
        if not vis[value]:
            change_value = BFS(graph, vis, value, change_value)
            for node in change_value:
                i, j = node
                matrix[i][j] = 'C'


if __name__ == '__main__':
    matrix = [['Y', 'Y', 'Y', 'G', 'G', 'G', 'G', 'G', 'G', 'G'],
              ['Y', 'Y', 'Y', 'Y', 'Y', 'Y', 'G', 'X', 'X', 'X'],
              ['G', 'G', 'G', 'G', 'G', 'G', 'G', 'X', 'X', 'X'],
              ['W', 'W', 'W', 'W', 'W', 'G', 'G', 'G', 'G', 'X'],
              ['W', 'R', 'R', 'R', 'R', 'R', 'G', 'X', 'X', 'X'],
              ['W', 'W', 'W', 'R', 'R', 'G', 'G', 'X', 'X', 'X'],
              ['W', 'B', 'W', 'R', 'R', 'R', 'R', 'R', 'R', 'X'],
              ['W', 'B', 'B', 'B', 'B', 'R', 'R', 'X', 'X', 'X'],
              ['W', 'B', 'B', 'X', 'B', 'B', 'B', 'B', 'X', 'X'],
              ['W', 'B', 'B', 'X', 'X', 'X', 'X', 'X', 'X', 'X']]

    main(matrix)

    file = open("Result_2.txt", 'w')

    for row in matrix:
        print(" ".join(row))
        file.write(" ".join(row))
