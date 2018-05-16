import pickle

__all__ = ['get_conjectures', 'sorted_conjectures',
            'limited_sorted_conjectures']


def get_conjectures(target, family):
    with open(target+'_'+family+'_conjectures', 'rb') as pickle_file:
        db = pickle.load(pickle_file)
    return db

def sorted_conjectures(target, family):
    db = get_conjectures(target, family)
    return sorted(db, key=lambda k: db[k]['touch'], reverse=True)

def limited_sorted_conjectures(target, family, limit):
    L = sorted_conjectures(target, family)
    return [L[i] for i in range(limit)]
