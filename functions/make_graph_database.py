from graph_txt_files.txt_functions.graph_calculator import calc
from graph_txt_files.txt_functions.graph_property_names import property_names
import grinpy as gp
import os
import pickle

__all__ = ['make_graph_db']

def make_graph_db(graph_type):

    graphs = [line[:-1] for
              line in os.popen('ls '+'graph_txt_files/graph_txt_folders/'+graph_type)]

    size = len(graphs)
    counter = 1
    pickle_dict = dict()
    for graph in graphs:
        pickle_dict[graph] =  dict()
        G = gp.read_edgelist('graph_txt_files/graph_txt_folders/'+graph_type+'/'+graph)
        for graph_property in property_names:
            pickle_dict[graph][graph_property] = calc(G, graph_property)

        print('Graph', counter, 'of', size)
        counter += 1

    pickle_out = open(graph_type, 'wb')
    pickle.dump(pickle_dict, pickle_out)
    pickle_out.close()

    return None
