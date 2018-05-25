import pickle
from classes.conjecture_class import Conjecture

#__all__ = ['remove_conjecture', 'transitivity_sweep', 'make_class']

def is_greater(conj1, conj2):
    graphs1 = conj1.conjecture_check[3]
    graphs2 = conj2.conjecture_check[3]
    A = []
    B = []
    for key in graphs1:
        A.appened(graphs1[key])
        B.append(graphs2[key])

    return A > B

def is_less(conj1, conj2):
    graphs1 = conj1.conjecture_check[3]
    graphs2 = conj2.conjecture_check[3]
    A = []
    B = []
    for key in graphs1:
        A.appened(graphs1[key])
        B.append(graphs2[key])
    return A < B

def transitivity_upper(conjectures, current_conj):

    for conj in conjectures:
        if conj != current_conj:
            if is_greater(conj, current_conj) == True:
                conjectures.remove(conj)
    return None

def transitivity_lower(conjectures, current_conj):

    for conj in conjectures:
        if conj != current_conj:
            if is_less(conj, current_conj) == True:
                conjectures.remove(conj)
    return None



def transitivity_sweep(conjectures,inequality = 'upper'):
    if inequality == 'upper':
        for conj in conjectures:
            transitivity_upper(conjectures, conj)
        return None

    else:
        transitivity_lower(conjectures, conj)
        return None
