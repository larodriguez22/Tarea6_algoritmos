import pytest
import algoritmo4
from copy import deepcopy

example_graph = [
    [1, 2, 3],
    [0, 2, 3],
    [0, 1],
    [0, 1]
]

def test_remove_random_vertex_from_edge():
    test_graph = deepcopy(example_graph)
    remove_result = algoritmo4.remove_random_vertex_from_edge(test_graph, (0, 1))
    assert remove_result == (0, [(0, 1), (0, 2), (0, 3), (1, 0), (2, 0), (3, 0)]) \
        or remove_result == (1, [(1, 2), (1, 3), (0, 1), (2, 1), (3, 1)])
    assert test_graph == [
            [],
            [2, 3],
            [1],
            [1]
        ] \
        or test_graph == [
            [2, 3],
            [],
            [0],
            [0]
        ]
    
def test_pick_random_edge():
    u, v = algoritmo4.pick_random_edge(example_graph)
    assert v in example_graph[u]

def test_graph_has_edges():
    assert algoritmo4.graph_has_edges(example_graph)
    assert not algoritmo4.graph_has_edges([[], [], []])

def test_vertex_cover():
    result = algoritmo4.algorithm4(example_graph)
    assert len(result) > 0