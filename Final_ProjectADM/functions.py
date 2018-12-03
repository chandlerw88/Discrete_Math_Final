# -*- coding: utf-8 -*-

#
from Weighted_Graph import *

G = Weighted_Graph('testG.txt')
G.draw_graph()
#print(G.edge_set())#List
#print(G.vertex_set())#Set
#print(G.edge_dict())#dictionary
#H=({0,1,3}, [(0,1),(1,3)])
#G.draw_subgraph(H)
#


def cost(e,G):
    return G.edge_dict()[e]
#Check Function
#print((c((1,4),G)))
T = ({2,3},[(2,3)])
def incident_edges(T,G):
    edges = []
    for v in T[0]:
        for e in G.edge_set():
            if v in e:
                edges.append(e)
        for e in edges:
            if e in T[1]:
                edges.remove(e)
    return edges        
        
                
print(incident_edges(T,G))

def min_incident_edge(T,G):
    edges = incident_edges(T,G)
    min_edge = edges[0]
    for e in edges:
        print(min_edge)
        print(e)
        print(f'is {cost(min_edge, G)} less that {cost(e,G)}?')
        if cost(min_edge,G) < cost(e,G): 
            min_edge = e
            print(min_edge)
        return min_edge
print(min_incident_edge(T,G))
    



    
    
    
    
    