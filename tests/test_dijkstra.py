# test_dijkstra.py
import pytest
import networkx as nx
from dsp.algorithms.dijkstra import dijkstra, reconstruct_path


@pytest.fixture
def sample_graph():
    # Adjacency list format for your function
    custom_graph = {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2), ("Z", 6)],
        "E": [("C", 10), ("D", 2), ("Z", 3)],
        "Z": [("D", 6), ("E", 3)],
    }
    # For networkx
    G = nx.Graph()
    for u, neighbors in custom_graph.items():
        for v, w in neighbors:
            G.add_edge(u, v, weight=w)
    return custom_graph, G


def test_distances_match_networkx(sample_graph):
    custom_graph, G = sample_graph
    source = "A"
    # Your implementation
    custom_distances, custom_preds = dijkstra(custom_graph, source)
    # Networkx's result
    nx_lengths, _ = nx.single_source_dijkstra(G, source, weight="weight")
    assert custom_distances == nx_lengths


def test_path_matches_networkx(sample_graph):
    custom_graph, G = sample_graph
    source, target = "A", "Z"
    _, custom_preds = dijkstra(custom_graph, source)
    custom_path = reconstruct_path(custom_preds, source, target)
    nx_path = nx.shortest_path(G, source, target, weight="weight", method="dijkstra")
    assert custom_path == nx_path
