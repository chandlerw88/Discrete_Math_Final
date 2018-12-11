# -*- coding: utf-8 -*-

"""
G.edge_set gives you edges as a list
G.vertex_set gives you edges as a set
G.edge_dict gives you everthing
For most points possible show tree being built using draw_subgraph

start with this:
    from Weighted_Graph import *
     G=Weighted_Graph('test_graph.txt')
     G.draw_graph()
      T=({3},[])


inside function.py:
    def c(e,G):
        return G.edge_dict()[e]     this allows us to not have to type a lot to get cost of an edge
        
        checked with:
            print(c((1,4),G))<---- G is a weighted graph
            
            Prims
            Initialize:
             1   T=({v},[])    T=({3},[])
                               T=({2,3},[(2,3)])  

incident edges formula
def: incident_edges(T,G): <----- T is a tree
        edges=[]
        for v in T[0]:
            for e in G.edge_set():
                if v in e:
                    edges.append(e)
            for e in edges
            if e in T[1]
                 edge.remove(e)               <----- Add the removing of a vertices to prevent cycling
        return edges


def: min_incident_edge(T,G):
    edges=incident_edges(T,G)
    min_edge=edges[0]
    for e in edges 
     if ___
    return mid_edge
    
def:update(T,G)
T[0]




Inside of prims.py:
    from Weighted_Graph import Weighted_Graph
    From functions import update
    
    def Prims(edge_file_name, start_vertex=0, draw = False):
        T=({start_vertex},[])
        G= Weighted_Graph(edge_file_name)   <<<BELOW THIS>>>if draw= true <<G.draw_graph()
        while T[0]!=G.vertex_set():
            update(T,G)
            if draw==True:
            G.draw_subgraph(T)
        return cost(T)
"""
