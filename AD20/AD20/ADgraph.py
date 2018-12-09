import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

def merge_dicts(d1, d2):
    dnew = d1.copy()
    for key in d2:
        if key in dnew:
            dnew[key] = dnew[key]+d2[key]
        else:
            dnew[key] = d2[key]
    return dnew

def gen_graph(y):
    G = nx.DiGraph()
    d = y.graph
    for key in d:
        G.add_node(key)
        neighbors = d[key]
        for neighbor in neighbors:
            G.add_edge(key, neighbor[0], label = neighbor[1])
    return G

def reverse_graph(y):
    d = y.graph


def draw_graph(y):
    fig = plt.figure()
    G = gen_graph(y)
    edge_labs = nx.get_edge_attributes(G, 'label')
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, with_labels = False)
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labs)
    limits = plt.axis('off')
    return fig

def plot_ADnum(x, xmin = -10, xmax = 10):
    vals = np.linspace(xmin, xmax, 100)
    evals = [x(value).val for value in vals]
    ders = [x(value).der for value in vals]
    fig = plt.figure()
    plt.plot(vals, evals, label = 'f', linewidth = 2)
    plt.plot(vals, ders, label = 'df/dx', linewidth = 2)
    plt.legend(fontsize = 20)
    plt.xlabel('x', fontsize = 20)
    plt.ylabel('f', fontsize = 20)
    return fig

#def gen_compgraph(d):
 #   G = nx.DiGraph()
  #  for key in d.keys():
   #     neighbors = d[key]
    #    for neighbor in neighbors:
     #       G.add_edge()
    #return G
