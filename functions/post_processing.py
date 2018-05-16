import pickle


__all__ = ['remove_noise', 'transitivity_sweep']

def is_greater(conj1, conj2, target, family):
    # Is conj1 always greater than conj2?

    with open(target+'_'+family+'_conjectures', 'rb') as pickle_file:
        db = pickle.load(pickle_file)
    with open(family, 'rb') as pickle_file:
        family = pickle.load(pickle_file)

    for graph in family:
        if db[conj1]['expression_values'][graph] < db[conj2]['expression_values'][graph]:
            return False
    return True

def is_less(conj1, conj2, target, family):
    # Is conj1 always less than conj2?

    with open(target+'_'+family+'_conjectures', 'rb') as pickle_file:
        db = pickle.load(pickle_file)
    with open(family, 'rb') as pickle_file:
        family = pickle.load(pickle_file)

    for graph in family:
        if db[conj1]['expression_values'][graph] > db[conj2]['expression_values'][graph]:
            return False
    return True

def remove_noise(conjectures, noise):
    for conj in conjectures:
        if noise in conj:
            conjectures.remove(conj)
        elif ' '+noise in conj:
            conjectures.remove(conj)
        elif '  '+noise in conj:
            conjectures.remove(conj)
        elif noise+' ' in conj:
            conjectures.remove(conj)
        elif noise+'  ' in conj:
            conjectures.remove(conj)
        elif ' '+noise+' ' in conj:
            conjectures.remove(conj)
    return None

def transitivity_upper(conjectures, current_conj, target, family):

    for conj in conjectures:
        if conj != current_conj:
            if is_greater(conj, current_conj, target, family) == True:
                conjectures.remove(conj)
    return None

def transitivity_lower(conjectures, current_conj, target, family):

    for conj in conjectures:
        if conj != current_conj:
            if is_less(conj, current_conj, target, family) == True:
                conjectures.remove(conj)
    return None



def transitivity_sweep(conjectures,target, family, inequality = 'upper'):
    if inequality == 'upper':
        for conj in conjectures:
            transitivity_upper(conjectures, conj, target, family)
        return None

    else:
        or conj in conjectures:
            transitivity_lower(conjectures, conj, target, family)
        return None
