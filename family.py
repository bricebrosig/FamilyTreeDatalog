"""python data log of the shakespeare family

supports queries for mothers, father, aunts, uncles, ancestors, sisters, and brothers
"""

male = [
    'John Shakespeare',
    'William Shakespeare',
    'Gilbert Shakespeare',
    'Richard Shakespeare',
    'Edmund Shakespeare',
    'Hamnet Shakespeare',
    'John Hall',
    'Thomas Quiney',
    'Shakespeare Quiney',
    'Richard Quiney',
    'Thomas II Quiney'
]

female = [
    'Mary Arden',
    'Margaret Shakespeare',
    'Anne Shakespeare',
    'Anne Hathaway',
    'Susanna Shakespeare',
    'Judith Shakespeare',
    'Elizabeth Hall'
]

parent_of = {
    'William Shakespeare': ['John Shakespeare', 'Mary Arden'],
    'Margaret Shakespeare': ['John Shakespeare', 'Mary Arden'],
    'Gilbert Shakespeare': ['John Shakespeare', 'Mary Arden'],
    'Joan Shakespeare': ['John Shakespeare', 'Mary Arden'],
    'Anne Shakespeare': ['John Shakespeare', 'Mary Arden'],
    'Richard Shakespeare': ['John Shakespeare', 'Mary Arden'],
    'Edmund Shakespeare': ['John Shakespeare', 'Mary Arden'],

    'Susanna Shakespeare': ['William Shakespeare', 'Anne Hathaway'],
    'Hamnet Shakespeare': ['William Shakespeare', 'Anne Hathaway'],
    'Judith Shakespeare': ['William Shakespeare', 'Anne Hathaway'],

    'Elizabeth Hall': ['John Hall', 'Susanna Shakespeare'],

    'Shakespeare Quiney': ['Thomas Quiney', 'Judith Shakespeare'],
    'Richard Quiney': ['Thomas Quiney', 'Judith Shakespeare'],
    'Thomas II Quiney': ['Thomas Quiney', 'Judith Shakespeare']
}


def sibling_of(X):
    def f():
        for item in parent_of.items():
            key, value = item
            if value == parent_of.get(X) and X != key:
                yield key

    return list(f())


def brother_of(X):
    def f():
        for sib in sibling_of(X):
            if sib in male:
                yield sib

    return list(f())


def sister_of(X):
    def f():
        for sib in sibling_of(X):
            if sib in female:
                yield sib

    return list(f())


def mother_of(X):
    def f():
        for par in parent_of.get(X):
            if par in female:
                yield par

    return list(f())


def father_of(X):
    def f():
        for par in parent_of.get(X):
            if par in male:
                yield par

    return list(f())


def gp_of(X):
    def f():
        for par in parent_of.get(X, []):
            for gp in parent_of.get(par, []):
                yield gp
    return list(f())


def ancestor_of(X):
    # FIXME: this don't work dad
    def f(y):
        if parent_of.get(y):
            return parent_of.get(y)
        else:
            for par in parent_of.get(y, []):
                yield ancestor_of(par)

    return list(f(X))


def cousin_of(X):
    def f():
        for gp in gp_of(X):
            for y in male + female:
                for other_gp in gp_of(y):
                    if other_gp == gp and y != X and y not in sibling_of(X):
                        yield y

    return list(set(f()))


def aunt_or_uncle_of(X):
    def f():
        for par in parent_of.get(X, []):
            for sib in sibling_of(par):
                yield sib

    return list(f())


def aunt_of(X):
    return [y for y in aunt_or_uncle_of(X) if y in female]


def uncle_of(X):
    return [y for y in aunt_or_uncle_of(X) if y in male]


# test cases here
# print(sibling_of('Susanna Shakespeare'))
# print(brother_of('Susanna Shakespeare'))
# print(sister_of('William Shakespeare'))
# print(mother_of('Hamnet Shakespeare'))
# print(father_of('Richard Quiney'))
# print(gp_of('Elizabeth Hall'))
print(ancestor_of('Shakespeare Quiney'))  # nocheckin
print(cousin_of('Elizabeth Hall'))  # nocheckin
# print(aunt_or_uncle_of('Thomas II Quiney'))
# print(aunt_of('Richard Quiney'))
# print(uncle_of('Susanna Shakespeare'))