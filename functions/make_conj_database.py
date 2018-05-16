from classes.conjecture_class import Conjecture
from functions.expressions import one_operation
from graph_txt_files.txt_functions.graph_property_names import property_names
import pickle

def make_possible_expressions(target):
    temp = []
    for name in property_names:
        if name != target:
            for expr in one_operation(name):
                temp.append(expr)
    return temp

def make_possible_inequalities(target, inequality):
    temp = []
    for x in make_possible_expressions(target):
        temp.append([target, inequality, x])
    return temp


def make_conjecture_dict(target, inequality, family):
    main_dict = dict()
    for x in make_possible_inequalities(target, inequality):

        conj = Conjecture(x[0],x[1],x[2], family)
        D = {'name': conj.get_string()}
        if conj.conjecture_check()[0] == True:
            D['target'] = target
            D['inequality'] = inequality
            D['expression'] = conj.get_expression()
            D['family'] = family
            D['touch'] = conj.conjecture_check()[1]
            D['sharp_examples'] = conj.conjecture_check()[2]
            D['expression_values'] = conj.conjecture_check()[3]


            main_dict[conj.get_string()] = D
    return main_dict


def initial_conjecture_db(target, inequality, family):
    pickle_out = open(target+'_'+family+'_conjectures', 'wb')
    pickle.dump(make_conjecture_dict(target, inequality, family),pickle_out)
    pickle_out.close()
    return None
