from random import randint, choice
from copy import deepcopy
import numpy as np

# In place operation.
# We assume edge exists.
def remove_random_vertex_from_edge(graph: list, edge: tuple) -> list:
    to_remove = choice(edge)
    other_removed_edges = [(to_remove, destiny) for destiny in graph[to_remove]]
    graph[to_remove] = []
    for vertex_index, edge_list in enumerate(graph):
        if to_remove in edge_list:
            graph[vertex_index].remove(to_remove)
            other_removed_edges.append((vertex_index, to_remove))
    return (to_remove, other_removed_edges)

# Assume graph has edges.
def pick_random_edge(graph):
    picked_edge_list, chosed_index = [], None
    while picked_edge_list == []:
        chosed_index = randint(0, len(graph)-1)
        picked_edge_list = graph[chosed_index]
    return (chosed_index, choice(picked_edge_list)) 

def graph_has_edges(graph):
    for vertex in graph:
        if vertex != []:
            return True
    return False

def algorithm4(graph):
    copied_graph = deepcopy(graph)
    vertex_cover = []
    while graph_has_edges(copied_graph):
        removed_vertex, removed_edges = remove_random_vertex_from_edge(
            copied_graph, pick_random_edge(copied_graph))
        vertex_cover.append(removed_vertex)
    return vertex_cover