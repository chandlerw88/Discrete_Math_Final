# -*- coding: utf-8 -*-

#
#from Weighted_Graph import *

#G = Weighted_Graph('testG.txt')
#G.draw_graph()
#print(G.vertex_set())#vertex
#print(G.edge_set())#List
#print(G.edge_dict())#dictionary
#H=({0,1,3}, [(0,1),(1,3)])
#G.draw_subgraph(H)
#


def cost(e,G):
    return G.edge_dict()[e]
#Check Function
#print((c((1,4),G)))
#T = ({2,3,5,6},[(2,3),(3,5),(3,6)])
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
        
                
#print(incident_edges(T,G))

def valid_edges(T,G):
    edges = incident_edges(T,G)
    for e in edges:
        if edges.count(e)>1:
            edges.remove(e)
            edges.remove(e)            
    
    return edges
#print(valid_edges(T,G))


def min_incident_edge(T,G):
    edges = valid_edges(T,G)
    min_edge= valid_edges(T,G)[0]
    min_edge_cost=cost((valid_edges(T,G)[0]),G)
    for e in edges:
        if min_edge_cost > cost(e,G):
            min_edge = e
    return min_edge
#print(min_incident_edge(T,G))
#print("done")
def update(T,G):
    addedge = min_incident_edge(T,G)
    T[1].append(addedge)
    for e in addedge:
        if e not in T[0]:
            T[0].add(e)
            
    return T
#print(update(T,G))

    
    