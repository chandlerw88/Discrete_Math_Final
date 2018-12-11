# -*- coding: utf-8 -*-
from Weighted_Graph import Weighted_Graph
from functions import min_incident_edge, update, cost
#G = Weighted_Graph('testG.txt')

def Prims(edge_file_name, start_vertex = 0, draw = False):
    T = ({start_vertex}, [])
    G = Weighted_Graph(edge_file_name)
    
    
    
    while T[0] != G.vertex_set():
        print(T[0])
        print(G.vertex_set())
        ...
        ...
        update(T,G)
        if draw == True:
            G.draw_subgraph(T)
        
        ...
        ...
        ...
    print("done")    
    return cost(T)