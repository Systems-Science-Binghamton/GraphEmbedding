import unittest
import networkx as nx
import igraph
import numpy as np
from scipy import sparse

from scripts.network_robustness import *
from scripts.k_core_decomposition import *


class Test(unittest.TestCase):
    def setUp(self, **params):
        G = nx.karate_club_graph()
        A = nx.adjacency_matrix(G)
        src, trg, _ = sparse.find(sparse.triu(A, 1))
        self.g = igraph.Graph(tuple(zip(src, trg)))
