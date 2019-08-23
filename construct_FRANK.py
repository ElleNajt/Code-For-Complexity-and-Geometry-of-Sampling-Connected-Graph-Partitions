# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 02:56:21 2019

@author: Lorenzo
"""
import networkx as nx
import matplotlib.pyplot as plt

def viz(graph, n = set()):
    for x in graph.nodes():
        if x in n:
            graph.node[x]["col"] = 'r'
        else:
            graph.node[x]["col"] = 'b'
    values = [graph.node[x]["col"] for x in graph.nodes()]
    for x in graph.nodes():
        graph.node[x]['pos'] = (x[0], x[1])
    nx.draw(graph, pos=nx.get_node_attributes(graph, 'pos'), node_size = 10, width = .5,  node_color=values,with_labels=True)
    plt.show()

m = 50
G = nx.grid_graph([m,m])
H = nx.triangular_lattice_graph(m,2*m - 2)
relabel = {}
for x in G.nodes():
    relabel[x] = ( x[0] , x[1] - m + 1)
G= nx.relabel_nodes(G, relabel)

####Here is the Frankengraph
F = nx.compose(G,H)


'''
for i in range(-m,m):
    value = 0
    for x in F.nodes():
        if x[1] == i:
            value += 1
    print(i,value)
'''

horizontal = []
for x in F.nodes():
    if x[1] < 0:
        horizontal.append(x)
        
'''
viz(F,horizontal)
len(horizontal) #= 380
len(F) #= 800
'''

vertical = []
for x in F.nodes():
    if x[0] < m/2:
        vertical.append(x)
'''
viz(F,vertical)
len(vertical) #= 400
'''

diagonal = []
for x in F.nodes():
    if 2*x[0] - x[1] <= m -3:
        diagonal.append(x)

'''
viz(F,diagonal)
len(diagonal)#=380

'''

'''
Outputs:
    
    F is the Frankengraph
    horizontal, vertical and diagonal are the three seed partitions
    viz(F,horizontal) shows thems


'''

viz(F,horizontal)
