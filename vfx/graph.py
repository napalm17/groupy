import matplotlib.pyplot as plt
import networkx as nx
from helpers import Algo
import numpy as np

class Graph:
    """
    A class representing a directed graph with vertices and edges.

    Attributes:
    - vertices (set): A set of vertices in the graph.
    - edges (list): A list of edges in the graph.
    - edge_generators (dict): A dictionary mapping edges to generators.
    """

    def __init__(self, vertices=None, edges=None):
        """
        Initialize a directed graph with given vertices and edges.

        Parameters:
        - vertices (list, optional): A list of vertices to add to the graph.
        - edges (list, optional): A list of edges to add to the graph. Each edge should be a tuple
                                   of the form (vertex1, vertex2, generator).
        """
        self.vertices = set(vertices) if vertices else set()
        self.edges = []
        self.edge_generators = {}

        if edges:
            for vertex1, vertex2, generator in edges:
                self.add_edge(vertex1, vertex2, generator)

    def add_vertex(self, vertex):
        """
        Add a vertex to the graph.

        Parameters:
        - vertex: The vertex to add.
        """
        self.vertices.add(vertex)

    def add_edge(self, vertex1, vertex2, generator):
        """
        Add a directed edge to the graph with an associated generator.

        Parameters:
        - vertex1: The start vertex of the edge.
        - vertex2: The end vertex of the edge.
        - generator: The generator used to create this edge.
        """
        self.edges.append((vertex1, vertex2))
        self.edge_generators[(vertex1, vertex2)] = generator

    @staticmethod
    def plot_inclusion_tree(edges, nodes):
        """Plots the inclusion graph as a tree."""
        G = nx.DiGraph()
        G.add_edges_from(edges)
        plt.figure(figsize=(8, 6))

        sizes = np.array([len(s) for s in nodes])
        _, y_coordinates = np.unique(sizes, return_inverse=True)
        x_coordinates = Algo.transform_indices(sizes)
        pos = {node: (x, y) for node, x, y in zip(nodes,x_coordinates, y_coordinates)}
        colors = plt.cm.viridis(np.array(y_coordinates) / np.max(y_coordinates))  # Normalize sizes to [0, 1] for colormap
        print(colors)
        print(sizes)
        nx.draw(G, pos, with_labels=True, node_size=2000, node_color=colors, font_size=8, font_weight='bold')
        plt.show()

    def plot(self):
        """
        Plot the directed graph with vertices and edges. Edges are colored based on the generator
        and a legend is included to indicate the generator colors.
        """
        # Create a NetworkX directed graph
        G = nx.DiGraph()
        G.add_nodes_from(self.vertices)
        G.add_edges_from(self.edges)

        # Get unique generators and create a color map
        unique_generators = list(set(self.edge_generators.values()))
        color_map = plt.get_cmap('Set1')
        generator_color_map = {gen: color_map(i) for i, gen in enumerate(unique_generators)}
        edge_color_values = [generator_color_map[self.edge_generators[edge]] for edge in list(G.edges())]

        # Draw the graph with edge colors
        try:
            pos = nx.planar_layout(G)
        except:
            pos = nx.shell_layout(G)

        nx.draw(G, pos, with_labels=True, node_color='black', edge_color=edge_color_values,
                node_size=500, font_size=10, font_color='white', arrows=True, edgecolors='black')

        # Create a legend
        handles = [plt.Line2D([0], [0], color=generator_color_map[gen], lw=2) for gen in unique_generators]
        labels = [f'Generator {gen}' for gen in unique_generators]
        plt.legend(handles=handles, labels=labels, title='Generators')
        plt.show()
