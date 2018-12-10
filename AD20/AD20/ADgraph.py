import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from AD20.ADnum_multivar_graph import ADnum

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
                new_names[node] = str(np.round(node.val, decimals=1))
            else:
                new_names[node] = 'X' + str(total)
                total = total - 1
            if node in parents:
                neighbors = parents[node]
                for neighbor in neighbors:
                    nodes.append(neighbor[0])
    return new_names

def get_colors(G, y, labs):
    colors = []
    for node in G:
        if node.constant:
            colors.append('blue')
        else:
            if node == y:
                colors.append('green')
            else:
                if labs[node] == 'X0':
                    colors.append('magenta')
                else:
                    colors.append('red')
    return colors

def get_sizes(G, y, labs):
    sizes = []
    for node in G:
        label = labs[node]
        sizes.append(len(label)*200)
    return sizes

def draw_graph(y):
    fig = plt.figure()
    G = gen_graph(y)
    edge_labs = nx.get_edge_attributes(G, 'label')
    pos = nx.spring_layout(G)
    labs = get_labels(y)
    nx.draw_networkx(G, pos, labels = labs, node_color = get_colors(G, y, labs), node_size = get_sizes(G, y, labs), font_color= 'white')
    nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_labs)
    limits = plt.axis('off')
    plt.show()
    return fig

def gen_table(y):
    parents = reverse_graph(y)
    labs = get_labels(y)
    visited = []
    data = {}
    data['Trace'] = []
    data['Elementary Operation']=[]
    data['Value']= []
    data['Derivative']=[]
    nodes = [y]
    while len(nodes)>0:
        node = nodes.pop()
        if node not in visited:
            if node.constant:
                visited.append(node)
            else:
                visited.append(node)
                data['Trace'].append(labs[node])
                data['Value'].append(node.val)
                data['Derivative'].append(node.der)
                if node in parents:
                    link = parents[node][0][1]
                    neighbors = parents[node]
                    for neighbor in neighbors:
                        nodes.append(neighbor[0])
                else:
                    link = 'input'
                data['Elementary Operation'].append(link)

    return pd.DataFrame.from_dict(data)

def plot_ADnum(x, xmin = -10, xmax = 10):
    '''Function to plot f and its derivative for single variable input'''
    vals = np.linspace(xmin, xmax, 100)
    evals = [x(ADnum(value, der=1)).val for value in vals]
    ders = [x(ADnum(value, der=1)).der for value in vals]
    fig = plt.figure()
    plt.plot(vals, evals, label = 'f', linewidth = 2)
    plt.plot(vals, ders, label = 'df/dx', linewidth = 2)
    plt.legend(fontsize = 20)
    plt.xlabel('x', fontsize = 20)
    plt.ylabel('f', fontsize = 20)
    plt.xticks(fontsize = 12)
    plt.yticks(fontsize = 12)
    return fig


