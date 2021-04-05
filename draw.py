import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


def draw_graph(matrix: np.array, way: list):
    person_count = matrix[0].size
    g = nx.Graph()
    edges = []
    for i in range(0, person_count):
        for j in range(0, person_count):
            if matrix[i][j]:
                edges.append([str(i), str(j)])

    g.add_edges_from(edges)
    pos = nx.spring_layout(g)
    plt.figure()
    nx.draw(g, pos, labels={node: node for node in g.nodes()})

    formatted_edge_labels = {(str(way[i]), str(way[i+1])): str(i+1)
                             for i in range(0, person_count - 1)}

    nx.draw_networkx_edge_labels(g, pos,
                                 edge_labels=formatted_edge_labels)

    plt.draw()
    plt.show()
