from graph_txt_files.txt_functions.graph_calculator import calc
from graph_txt_files.txt_functions.graph_property_names import property_names
import grinpy as gp
import os
import pickle


exceptions = ['randic_index',
                'augmented_randic_index',
                'harmonic_index',
                'atom_bond_connectivity_index',
                'sum_connectivity_index',
                'min_degree',
                'max_degree',
                'number_of_min_degree_nodes',
                'number_of_max_degree_nodes']


__all__ = ['make_graph_db', 'exceptions']

def make_graph_db(graph_type):

    if graph_type == 'cubic':
        property_names_valid = [x for x in property_names if x not in exceptions]
    else:
        property_names_valid = property_names

    graphs = [line[:-1] for
              line in os.popen('ls '+'graph_txt_files/graph_txt_folders/'+graph_type)]

    size = len(graphs)
    counter = 1
    pickle_dict = dict()
    for graph in graphs:
        pickle_dict[graph] =  dict()
        G = gp.read_edgelist('graph_txt_files/graph_txt_folders/'+graph_type+'/'+graph)
        for graph_property in property_names_valid:
            pickle_dict[graph][graph_property] = calc(G, graph_property)
        print('Graph', counter, 'of', size)
        counter += 1

    pickle_out = open(graph_type, 'wb')
    pickle.dump(pickle_dict, pickle_out)
    pickle_out.close()

    return None
