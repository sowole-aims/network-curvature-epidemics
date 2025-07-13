import numpy as np
import networkx as nx

# Class to compute Forman-Ricci curvature for directed networks
class FormanRicciDirected:
    """
    Compute the Forman-Ricci curvature for all edges in a directed network.
    Also computes the In and Out Forman curvature for all nodes.
    """
    def __init__(self, G):
        self.G = G.copy()

    # Method to compute Forman-Ricci curvature for edges
    def compute_ricci_curvature(self):
        if not self.G.is_directed():
            raise ValueError("The graph must be directed.")

        edge_curvature = {}  # Dictionary to store curvature for each edge

        # Iterate through all edges in the graph
        for u, v in self.G.edges():
            w_e = self.G[u][v].get('weight', 1)  # Weight of the edge
            w_u = self.G.nodes[u].get('weight', 1)  # Weight of the source node
            w_v = self.G.nodes[v].get('weight', 1)  # Weight of the target node

            sum_u = 0  # Sum term for the source node
            sum_v = 0  # Sum term for the target node

            # Sum over the edges outgoing from the source node
            for _, u_neigh in self.G.out_edges(u):
                if u_neigh != v:
                    w_u_neigh = self.G[u][u_neigh].get('weight', 1)
                    sum_u += w_u / np.sqrt(w_e * w_u_neigh)

            # Sum over the edges incoming to the target node
            for v_neigh, _ in self.G.in_edges(v):
                if v_neigh != u:
                    w_v_neigh = self.G[v_neigh][v].get('weight', 1)
                    sum_v += w_v / np.sqrt(w_e * w_v_neigh)

            # Calculate Forman-Ricci curvature for the edge
            F_e = w_e * (w_u / w_e - sum_u) + w_e * (w_v / w_e - sum_v)
            edge_curvature[(u, v)] = F_e

        # Set edge attributes for the graph
        nx.set_edge_attributes(self.G, edge_curvature, 'FormanCurvature')

        return self.G

    # Method to compute In and Out Forman-Ricci curvatures for nodes
    def compute_node_curvatures(self):
        F_I = {v: 0 for v in self.G.nodes()}  # Dictionary for In Forman-Ricci curvature
        F_O = {v: 0 for v in self.G.nodes()}  # Dictionary for Out Forman-Ricci curvature

        # Iterate through all edges to calculate node curvatures
        for u, v in self.G.edges():
            F_e = self.G[u][v]['FormanCurvature']
            F_I[v] += F_e  # Sum of incoming edges for target node
            F_O[u] += F_e  # Sum of outgoing edges for source node

        # Set node attributes for the graph
        nx.set_node_attributes(self.G, F_I, 'FormanCurvatureIn')
        nx.set_node_attributes(self.G, F_O, 'FormanCurvatureOut')

        return self.G