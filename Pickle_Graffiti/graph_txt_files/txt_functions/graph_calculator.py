import networkx as nx
import grinpy as GPY
from graph_txt_files.txt_functions.triameter import triameter
from graph_txt_files.txt_functions.domination import domination_number, total_domination_number
from graph_txt_files.txt_functions.domination import independent_domination_number
from graph_txt_files.txt_functions.chromatic_number import chromatic_number
from graph_txt_files.txt_functions.matching_number import matching_number
from graph_txt_files.txt_functions.vertex_cover_number import vertex_cover_number
from graph_txt_files.txt_functions.independence_number import independence_number
from graph_txt_files.txt_functions.topological_indicies import *




def calc(G, invariant):
    if invariant == 'domination_number':
        return domination_number(G)
    elif invariant == 'chromatic_number':
        return chromatic_number(G)
    elif invariant == 'total_domination_number':
        return total_domination_number(G)
    elif invariant == 'connected_domination_number':
        return GPY.connected_domination_number(G)
    elif invariant == 'independent_domination_number':
        return independent_domination_number(G)
    elif invariant == 'slater':
        return GPY.slater(G)
    elif invariant == 'sub_total_domination_number':
        return GPY.sub_total_domination_number(G)
    elif invariant == 'annihilation_number':
        return GPY.annihilation_number(G)
    elif invariant == 'independence_number':
        return independence_number(G)
    elif invariant == 'power_domination_number':
        return GPY.power_domination_number(G)
    elif invariant == 'residue':
        return GPY.residue(G)
    elif invariant == 'k_residual_index':
        return GPY.k_residual_index(G)

    elif invariant == 'connected_zero_forcing_number':
        return GPY.connected_zero_forcing_number(G)
    elif invariant == 'total_zero_forcing_number':
        return GPY.total_zero_forcing_number(G)
    elif invariant == 'zero_forcing_number':
        return GPY.zero_forcing_number(G)

    elif invariant == 'diameter':
        return nx.diameter(G)
    elif invariant == 'radius':
        return nx.radius(G)

    elif invariant == 'order':
        return nx.number_of_nodes(G)
    elif invariant == 'size':
        return nx.number_of_edges(G)

    elif invariant == 'min_degree':
        return GPY.min_degree(G)
    elif invariant == 'max_degree':
        return GPY.max_degree(G)

    elif invariant == 'number_of_min_degree_nodes':
        return GPY.number_of_min_degree_nodes(G)
    elif invariant == 'number_of_degree_one_nodes':
        return GPY.number_of_degree_one_nodes(G)
    elif invariant == 'number_of_max_degree_nodes':
        return GPY.number_of_max_degree_nodes(G)
    elif invariant == 'clique_number':
        return GPY.clique_number(G)
    elif invariant == 'min_maximal_matching_number':
        return GPY.min_maximal_matching_number(G)
    elif invariant == 'matching_number':
        return matching_number(G)
    elif invariant == 'triameter':
        return triameter(G)
    elif invariant == 'vertex_cover_number':
        return vertex_cover_number(G)



    elif invariant == 'randic_index':
        return randic_index(G)
    elif invariant == 'augmented_randic_index':
        return augmented_randic_index(G)
    elif invariant == 'harmonic_index':
        return harmonic_index(G)
    elif invariant == 'atom_bond_connectivity_index':
        return atom_bond_connectivity_index(G)

    elif invariant == 'sum_connectivity_index':
        return sum_connectivity_index(G)


    else:
        print('ERROR')
        return False
