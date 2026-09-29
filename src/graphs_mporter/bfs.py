from collections import deque


def bfs(graph, start):
    visited = []
    queue = deque([start])
    seen = {start}

    while queue:
        vertex = queue.popleft()
        visited.append(vertex)

        for neighbor in graph.get(vertex, {}):
            if neighbor not in seen:
                seen.add(neighbor)
                queue.append(neighbor)

    return visited