def bfs(graph, root):
    v1 = set()
    q = []
    q.append(root)
    q.extend(graph[root])

    while q:
        v2 = q.pop(0)
        if v2 not in v1:
            v1.add(v2)
            print(v2)
        for adj in graph[v2]:
            if adj not in v1:
                q.append(adj)
                

def dfs(visited, graph, root):
    if root not in visited:
        visited.add(root)
        print(root, " ")

        for adj in graph[root]:
            dfs(visited, graph, adj)


# graph = { 1: [3, 2], 2: [1, 4],  3: [1], 4: [2] }
graph = {0: [1, 2, 3], 1: [0], 2: [0, 3, 4, 5], 3: [0, 2], 4: [2, 5], 5: [2, 4]}
visited = set() 

print("Bfs: ")
bfs(graph, 0)
print()
print("Dfs: ")
dfs(visited, graph, 1)
