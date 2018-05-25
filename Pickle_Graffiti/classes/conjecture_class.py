import pickle
from sympy import sympify


class Conjecture:

    def __init__(self, target, inequality, expression, family):
        self.target = target
        self.inequality = inequality
        self.expression = expression.split()
        self.family_name = family
        self.family = pickle.load(open(family, 'rb'))

    def get_inequality(self):
        if self.inequality == 'upper':
            return ' <= '
        elif self.inequality == 'lower':
            return ' >= '
        else:
            print('ERROR: Inequality not detected')

    def get_expression(self):
        s = ''
        for string in self.expression:
            s+= string
            s+= ' '
        return s

    def get_string(self):
        return f'{self.target} {self.get_inequality()} {sympify(self.get_expression())}'

    def __str__(self):
        if self.family_name == 'small_connected':
            return f'If G is a connected graph, then {self.get_string()}'
        elif self.family_name == 'tree':
            return f'If G is a tree, then {self.get_string()}'
        else:
            return f'If G is a connected and {self.family_name} graph, then {self.get_string()}'

    def target_value(self, G):
        return G[self.target]

    def expression_value(self, G):
        string = ''
        for invariant in self.expression:
            if invariant in G:
                string += str(G[invariant])
                string += ' '
            else:
                string += invariant
                string += ' '
        string +=' +.0'
        try: return eval(string)
        except ZeroDivisionError: return 0

    def conjecture_instance(self, G):
        return eval(str(self.target_value(G))+self.get_inequality()+
                    str(self.expression_value(G)))

    def conjecture_sharp(self, G):
        return self.target_value(G) == self.expression_value(G)


    def conjecture_check(self):
        t = 0
        tight = []
        value_dict = dict()
        for G in self.family:
            value_dict[G] = self.expression_value(self.family[G])
            if self.conjecture_instance(self.family[G]) == False:
                return (False, 0)
            elif self.target_value(self.family[G]) == self.expression_value(self.family[G]):
                t += 1
                tight.append(G)
        return (True, t, tight, value_dict)


    def touch(self):
        t = 0
        for G in self.family:
            t += int(self.conjecture_sharp(self.family[G]))
        return t


    def conjecture_check_sharp(self):
        return self.touch() > 1 and self.conjecture_check()[0]

    def __eq__(self, other):
        if self.get_expression() == other.get_expression():
            return True
        else:
            return False
