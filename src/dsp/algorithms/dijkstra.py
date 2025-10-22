"""
dijkstra.py
------------
Custom implementation of Dijkstra's algorithm for finding the shortest
paths from a source node to all other reachable nodes in a weighted graph.

The graph should be represented as an adjacency list:
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        ...
    }

Author: Shashwat Kumar
"""

import heapq


def dijkstra(graph, source):
    """
    Compute shortest paths and distances from source to all nodes using Dijkstra's
    algorithm.

    Args:
        graph (dict): Adjacency list representation.
                      Keys are node IDs, values are lists of (neighbor, weight) pairs.
        source: The node to start from.

    Returns:
        distances (dict): Shortest distances from source to each node.
        predecessors (dict): Previous node in the optimal path from source.
    """
    # Initialize all distances to infinity, source to 0
    distances = {node: float("inf") for node in graph}
    predecessors = {node: None for node in graph}
    distances[source] = 0

    # Min-heap priority queue: (distance, node)
    heap = [(0, source)]
    visited = set()

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            if neighbor in visited:
                continue
            new_dist = current_dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                predecessors[neighbor] = current_node
                heapq.heappush(heap, (new_dist, neighbor))

    return distances, predecessors


def reconstruct_path(predecessors, source, target):
    """
    Reconstruct the shortest path from source to target using the
    predecessors dictionary.

    Args:
        predecessors (dict): Output from dijkstra(), maps node to its predecessor.
        source: The start node.
        target: The end node.

    Returns:
        path (list): List of nodes from source to target (inclusive), or empty if
        unreachable.
    """
    path = []
    node = target

    while node is not None:
        path.append(node)
        if node == source:
            break
        node = predecessors[node]

    path.reverse()
    if path[0] == source:
        return path
    return []
