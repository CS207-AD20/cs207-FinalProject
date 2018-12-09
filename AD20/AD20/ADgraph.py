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
    parents = {}
    for key in d:
        neighbors = d[key]
        for neighbor in neighbors:
            if neighbor[0] not in parents:
                parents[neighbor[0]] = []
            parents[neighbor[0]].append((key, neighbor[1]))
    return parents

def get_labels(y):
    parents = reverse_graph(y)
    total = len(y.graph) - sum([entry.constant for entry in y.graph.keys()])
    new_names = {}
    nodes = [y]
    while len(nodes)>0:
        node = nodes.pop()
        if node not in new_names:
            if node.constant:
                new_names[node] = str(node.val)
            else:
                new_names[node] = 'x' + str(total)
                total = total - 1
            if node in parents:
                neighbors = parents[node]
                for neighbor in neighbors:
                    nodes.append(neighbor[0])
    return new_names

def get_colors(G):
    colors = []
    for node in G:
        if node.constant:
            colors.append('blue')
        else:
            colors.append('red')
    return colors



def draw_graph(y):
    fig = plt.figure()
    G = gen_graph(y)
    edge_labs = nx.get_edge_attributes(G, 'label')
    pos = nx.spring_layout(G)
    nx.draw_networkx(G, pos, labels = get_labels(y), node_color = get_colors(G))
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labs)
    limits = plt.axis('off')
    plt.show()
    return fig

def plot_ADnum(x, xmin = -10, xmax = 10):
    '''Function to plot f and its derivative for single variable input'''
    vals = np.linspace(xmin, xmax, 100)
    evals = [x(value).val for value in vals]
    ders = [x(value).der for value in vals]
    fig = plt.figure()
    plt.plot(vals, evals, label = 'f', linewidth = 2)
    plt.plot(vals, ders, label = 'df/dx', linewidth = 2)
    plt.legend(fontsize = 20)
    plt.xlabel('x', fontsize = 20)
    plt.ylabel('f', fontsize = 20)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    return fig


