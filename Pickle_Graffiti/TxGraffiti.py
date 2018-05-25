from pyfiglet import figlet_format
from halo import Halo
import time
from datetime import datetime, timedelta
import pygame
from functions.get_conjectures import get_conjectures, remove_duplicates
import pickle

valid_invariants = {1:'domination_number',
                    2:'total_domination_number',
                    3:'connected_domination_number',
                    4:'independence_number',
                    5:'power_domination_number',
                    6:'zero_forcing_number',
                    7:'total_zero_forcing_number',
                    8:'connected_zero_forcing_number',
                    9:'independent_domination_number',
                    10:'chromatic_number',
                    11:'matching_number',
                    12:'min_maximal_matching_number',
                    13:'clique_number'}

graph_properties = ['triameter',
                    'randic_index',
                    'augmented_randic_index',
                    'harmonic_index',
                    'atom_bond_connectivity_index',
                    'sum_connectivity_index',
                    'min_degree',
                    'max_degree',
                    'number_of_min_degree_nodes',
                    'number_of_max_degree_nodes',
                    'diameter',
                    'radius',
                    'order',
                    'size']

graph_families = {1:'small_connected',
                  2:'cubic'}#,
                  #3:'triangle_free',
                  #4:'claw_free',
                  #5:'triangulation',
                  #6:'polyhedral',
                  #7:'tree'}

__version__ = '0.0.2'

def main():
    print(figlet_format('TxGraffiti', font='slant'))
    print(figlet_format(' - LIGHT', font='slant'))
    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2018 Randy Davila')
    print()

    print('The invariants you may conjecture against are: ')
    print('----------------------------------------')
    print()
    i = 1
    for x in valid_invariants:
        print(str(i)+'.', valid_invariants[x])
        i+=1
        print()
    print('----------------------------------------')
    print()
    invariant = valid_invariants[int(input('Invariant: '))]
    print()

    print('The families of graphs you may conjecture against are: ')
    print('----------------------------------------')
    print()
    i = 1
    for x in graph_families:
        print(str(i)+'.', graph_families[x])
        i +=1
        print()
    print('---------------------------------------------')
    family = graph_families[int(input('Graph family: '))]
    print()
    print('---------------------------------------------')
    print()


    print()
    print(figlet_format('TxGraffiti', font='slant'))
    print(figlet_format(' - LIGHT', font='slant'))

    print('Version ' + __version__)
    print('Copyright ' + u'\u00a9' + ' 2018 Randy Davila')
    print()

    try:
        with open(f'{invariant}_{family}_conjectures', 'rb') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error, '. Please make desired database.')
        return None

    conjectures = get_conjectures(invariant, family)
    U = remove_duplicates(conjectures['upper'])
    L = remove_duplicates(conjectures['lower'])

    print('Upper Bounds')
    for i in range(1, 10):
        print(f'Conjecture {i}. {U[i]}')
        print('')
    print()
    print('Lower Bounds')
    for i in range(1, 10):
        print(f'Conjecture {i}. {L[i]}')
        print('')
    print()

    work = input('Remove conjectures? (y/n) ')
    while work == 'y':
        type = input('Upper or lower? (U/L) ')
        index = int(input('Conjecture label? '))
        if type == 'U':
            U.pop(index)
        else:
            L.pop(index)
        print('Upper Bounds')
        for i in range(1, 10):
            print(f'Conjecture {i}. {U[i]}')
            print('')
        print()
        print('Lower Bounds')
        for i in range(1, 10):
            print(f'Conjecture {i}. {L[i]}')
            print('')
        print()



        work = input('Remove conjectures? (y/n) ')

    f = open(f'{invariant}_{family}_conjectures', 'wb')
    conj_dict = {'upper': U, 'lower': L}
    pickle.dump(conj_dict, f)
    f.close()
    return 0


if __name__ == '__main__':
    main()
