# graphs_mporter

`graphs_mporter` is a Python library containing graph-related algorithms for CS3250 Software Development Methods & Tools.

The library includes an implementation of Dijkstra's shortest path algorithm using a min-heap. Dijkstra's algorithm finds the shortest distance from a starting vertex to every other reachable vertex in a weighted graph.

The library also includes a breadth-first search algorithm for traversing a graph.

## Repository

https://github.com/milesporter91/CS3250---Homework-5

## Installation

Clone the repository and install the package from the project directory:

```bash
pip install .
```

For development, the package can also be installed in editable mode:

```bash
pip install -e .
```

## Usage

Import the shortest path module:

```python
from graphs_mporter import sp
```

Graphs are represented as dictionaries where each vertex contains its neighboring vertices and their edge weights.

Example:

```python
graph = {
    0: {1: 4, 7: 8},
    1: {0: 4, 2: 8, 7: 11},
    2: {1: 8}
}

dist, path = sp.dijkstra(graph, 0)

print(dist)
print(path)
```

`dist` contains the shortest known distance from the source vertex to each vertex.

`path` contains the vertices used to reach each destination along its shortest path.

## Breadth-First Search

Import the BFS module:

```python
from graphs_mporter import bfs
```

Example:

```python
graph = {
    0: {1: 1, 2: 1},
    1: {3: 1},
    2: {4: 1},
    3: {},
    4: {}
}

visited = bfs.bfs(graph, 0)

print(visited)
```

Breadth-first search explores vertices level by level starting from the selected source vertex.

## Project Structure

```text
src/
└── graphs_mporter/
    ├── __init__.py
    ├── heapq.py
    ├── sp.py
    └── bfs.py
test.py
README.md
pyproject.toml
```

## Author

Miles Porter