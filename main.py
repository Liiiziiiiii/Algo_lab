import copy
from collections import defaultdict


def is_similar(strq1, str2):
    for i in range(len(strq1)):
        if strq1[:i] + strq1[i + 1:] == str2:
            return True

    return False


def similar(strq1, str2, m, n, dp):
    if m == 0 or n == 0:
        return 0

    if dp[m][n] != -1:
        return dp[m][n]

    if strq1[m - 1] == str2[n - 1]:
        dp[m][n] = 1 + similar(strq1, str2, m - 1, n - 1, dp)
        return dp[m][n]

    dp[m][n] = max(similar(strq1, str2, m, n - 1, dp), similar(strq1, str2, m - 1, n, dp))
    return dp[m][n]


def build_graph(arr):
    graph = defaultdict(list)
    n = len(arr)
    count = 0

    number = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m = len(arr[i])
        copy_arr = [word for word in arr[:i] + arr[i + 1:] if len(word) == m - 1]
        for y in range(len(copy_arr)):
            count += 1
            k = len(copy_arr[y])
            # print("copy_arr[i] - ", arr[i], "         ||           copy_arr[y]", copy_arr[y])
            cheak = is_similar(arr[i], copy_arr[y])
            if k == m - 1 and cheak:
                number[i][y] = similar(arr[i], copy_arr[y], m, k, [[-1] * (k + 1) for _ in range(m + 1)])
                # print(arr[i], " + ", copy_arr[y], " = ", number[i][y], cheak)
                if number[i][y] > 0:
                    graph[arr[i]].append((copy_arr[y], number[i][y]))
    print("build_graph ", count)

    return graph


def find_chain(graph, start_word):
    count = 1
    start_nodes = [start_word]

    def compare_nodes(node1, node2):
        weight1 = max(graph[node1], key=lambda x: x[1])[1] if node1 in graph else 0
        weight2 = max(graph[node2], key=lambda x: x[1])[1] if node2 in graph else 0

        if weight1 != weight2:
            return weight1 - weight2
        else:
            return len(node2) - len(node1)

    for start_node in start_nodes:
        current_node = start_node
        chain = [current_node]

        while current_node in graph:
            next_node = max(graph[current_node], key=lambda x: compare_nodes(x[0], current_node))[0]
            chain.append(next_node)
            current_node = next_node
            count += 1

        # print(" > ".join(chain))

    return chain


def find_chain_all(graph):
    max_len = 0
    for current in graph:
        current_chain = find_chain(graph, current)
        max_len = max(max_len, len(current_chain))

        if len(current_chain) >= 7:
            print(current, "         -----------------------")
            print(current, len(current_chain))
            print(" > ".join(current_chain))


file_path = "input.txt"
with open(file_path, 'r') as file:
    arr = [line.strip() for line in file]

graph = build_graph(arr)
# find_chain(graph, "crates")


# find_chain(graph, "breasts")
find_chain_all(graph)


