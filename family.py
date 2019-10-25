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
    ...

def brother_of(X):
    ...

def sister_of(X):
    ...

def mother_of(X):
    ...

def father_of(X):
    pass

def gp_of(X):
    pass

def ancestor_of(X):
    pass

def cousin_of(X):
    pass

def aunt_of_uncle_of(X):
    pass

def aut_of(X):
    pass

def uncle_of(X):
    pass

# test cases here
sibling_of('Susanna Shakespeare')
