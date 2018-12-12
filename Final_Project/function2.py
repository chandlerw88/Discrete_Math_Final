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
    edges=incident_edges(T,G)
    valid_e = []
    for e in edges:
        if e[0] not in T[0] or e[1] not in T[0]:
            valid_e.append(e)
    return valid_e
    
    
    
def min_incident_edge(T,G):
    edges = valid_edges(T,G)

    min_e=edges[0]
    for e in edges:
        if cost(min_e,G) > cost(e,G): 
            min_e = e
    return min_e


def updateT(T,G):
    e = min_incident_edge(T,G)
    for v in e:
        T[0].add(v)
    T[1].append(e)
    
    return None

    