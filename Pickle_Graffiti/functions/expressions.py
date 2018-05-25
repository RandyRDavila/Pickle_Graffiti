
# -*- coding: utf-8 -*-

#    Copyright (C) 2018 by
#    Randy Davila <davilar@uhd.edu>
#    BSD license.
#
# Authors: Randy Davila <davilar@uhd.edu>

"""
            Functions that generate possible expressions for which a given
            graph invariant will be tested against.
"""


__all__ =['one_ratio', 'one_addition', 'one_operation']

def one_ratio(x):
    return [x,
            x+' /2',
            x+' /3',
            x+' /4',
            x+' / radius',
            x+' * radius',
            x+' / ( radius + 1)',
            x+' * ( radius + 2)',
            x+' / triameter',
            x+' * triameter',
            'order / '+x,
            'size / '+x,
            '2 * '+x+' /3',
            '3 * '+x+' /2',
            '2 * '+x+' /5',
            '5 * '+x+' /2',
            '3 * '+x+' /4',
            '4 * '+x+' /3',
            '3 * '+x+' /5',
            '5 * '+x+' /3',
            '5 * '+x+' /8',
            '3 * '+x+' /8',
            '7 * '+x+' /4'
            ]

def one_addition(x):
    return ['( '+x+' - 1)',
            '( '+x+' + 1)',
            '( '+x+' - 2)',
            '( '+x+' + 2)',
            '( '+x+' - 3)',
            '( '+x+' + 3)',
            '( '+x+' + 4)',
            '( '+x+' - 4)',
            '( '+x+' + order )'
            ]


def one_operation(x):
    X = one_ratio(x)
    Y = one_addition(x)

    result = []
    for x in X:
        result.append(x)
        for r in one_addition(x):
            result.append(r)
    for y in Y:
        result.append(y)
        for w in one_ratio(y):
            result.append(w)

    return result
