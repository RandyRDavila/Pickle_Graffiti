from classes.conjecture_class import Conjecture
from functions.expressions import one_operation
from functions.make_graph_database import exceptions
from graph_txt_files.txt_functions.graph_property_names import property_names
import pickle

__all__ = ['make_conjectures',
           'conjecture_db']

def make_expressions(target, family):
    temp = []
    if family == 'cubic':
        property_names_valid = [x for x in property_names if x not in exceptions]
    else:
        property_names_valid = property_names

    for name in property_names_valid:
        if name != target:
            for expr in one_operation(name):
                temp.append(expr)
    return temp

def make_inequalities(target, inequality, family):
    temp = []
    for x in make_expressions(target, family):
        temp.append([target, inequality, x])
    return temp

def make_conjectures(target, inequality, family):
    main_list = []
    for x in make_inequalities(target, inequality, family):
        conj = Conjecture(x[0],x[1],x[2], family)
        if conj.conjecture_check_sharp() == True:
            main_list.append(conj)
    return sorted(main_list, key = lambda k: k.touch(), reverse =True)

def conjecture_db(target, family):
    conj_dict = {'upper': make_conjectures(target, 'upper', family),
                'lower': make_conjectures(target, 'lower', family)
                }
    pickle_out = open(f'{target}_{family}_conjectures', 'wb')
    pickle.dump(conj_dict, pickle_out)
    pickle_out.close()
    return None
