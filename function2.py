# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 17:00:38 2018

@author: chand
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27 18:14:29 2018
@author: chand
"""

def cost(e,G):
        return G.edge_dict()[e] 

def incident_edges(T,G):
        edges=[]
        for v in T[0]:
            for e in G.edge_set():
                if v in e:
                    edges.append(e)
            for e in edges:
                if e in T[1]:
                 edges.remove(e) 
        return edges

def valid_edges(T,G):
    edges=[]
    for v in T[0]:
        for e in incident_edges(T,G):
            if v in e:
                edges.append(e)
    for e in T[1]:
     for x in e:
        if x not in T[0]:
            for i in edges:
                if x in i:
                    edges.remove(i)
    return edges

def min_incident_edge(T,G):
    edges = valid_edges(T,G)
    min_edge=valid_edges(T,G)[0]
    min_edge_cost=cost((valid_edges(T,G)[0]),G)
    for e in edges:
        if min_edge_cost > cost(e,G): 
            min_edge = e
    return min_edge


def updateT(T,G):
    edges=min_incident_edge(T,G)
    T[1].append(edges)
    current_vert=list(T[0])[0]
    if len(T[1]) > 0:
        nextEdge=list(T[1])[-1]
        for v in nextEdge:
            if v != current_vert:
                T[0].clear()
                T[0].add(v)            
    return T