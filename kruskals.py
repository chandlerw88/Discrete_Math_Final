# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 18:37:07 2018

@author: chand
"""
from Weighted_Graph import *
from function2 import*


def Kruskals(edge_file_name, start_vertex=0, draw = False):
        T=({start_vertex},[])
        G= Weighted_Graph(edge_file_name)   
        while T[1]!=len(G.vertex_set())-1:
            updateT(T,G)
            if draw==True:
                G.draw_subgraph(T)
        return cost(T)