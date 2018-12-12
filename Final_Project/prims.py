

from Weighted_Graph import Weighted_Graph
from function2 import updateT, cost

def Prims(edge_list, start_vertex = 0, show=False):
    G = Weighted_Graph(edge_list)
    T = ({start_vertex}, [])
    
    if show == True:
        G.draw_graph()
        
    # Prims Algorithm
    while T[0] != G.vertex_set():
        updateT(T, G)
        if show == True:
            G.draw_subgraph(T)
        
    return f'The optimal cost of the MST: {sum([cost(e,G) for e in T[1]])}'

print(Prims('test_graph.txt', show=True))