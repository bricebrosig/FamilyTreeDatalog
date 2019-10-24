c:-['family.pro'].

% facts about the shakespeare family

male('John Shakespeare').
male('William Shakespeare').
male('Gilbert Shakespeare').
male('Richard Shakespeare').
male('Edmund Shakespeare').
male('Hamnet Shakespeare').
male('John Hall').
male('Thomas Quiney').
male('Shakespeare Quiney').
male('Richard Quiney').
male('Thomas II Quiney').

female('Mary Arden').
female('Margaret Shakespeare').
female('Anne Shakespeare').
female('Anne Hathaway').
female('Susanna Shakespeare').
female('Judith Shakespeare').
female('Elizabeth Hall').

%john and mary ardens children
parent_of('William Shakespeare', 'John Shakespeare').
parent_of('William Shakespeare', 'Mary Arden').
parent_of('Margaret Shakespeare', 'John Shakespeare').
parent_of('Margaret Shakespeare', 'Mary Arden').
parent_of('Gilbert Shakespeare', 'John Shakespeare').
parent_of('Gilbert Shakespeare', 'Mary Arden').
parent_of('Joan Shakespeare', 'John Shakespeare').
parent_of('Joan Shakespeare', 'Mary Arden').
parent_of('Anne Shakespeare', 'John Shakespeare').
parent_of('Anne Shakespeare', 'Mary Arden').
parent_of('Richard Shakespeare', 'John Shakespeare').
parent_of('Richard Shakespeare', 'Mary Arden').
parent_of('Edmund Shakespeare', 'John Shakespeare').
parent_of('Edmund Shakespeare', 'Mary Arden').

%willian and anne hathaways children
parent_of('Susanna Shakespeare', 'William Shakespeare').
parent_of('Susanna Shakespeare', 'Anne Hathaway').
parent_of('Hamnet Shakespeare', 'William Shakespeare').
parent_of('Hamnet Shakespeare', 'Anne Hathaway').
parent_of('Judith Shakespeare', 'William Shakespeare').
parent_of('Judith Shakespeare', 'Anne Hathaway').

%children of susanna and john Hall
parent_of('Elizabeth Hall', 'John hall').
parent_of('Elizabeth Hall', 'Susanna Shakespeare').

%children of judith and thomas quiney.
parent_of('Shakespeare Quiney', 'Thomas Quiney').
parent_of('Shakespeare Quiney', 'Judith shakespeare').
parent_of('Richard Quiney', 'Thomas Quiney').
parent_of('Richard Quiney', 'Judith shakespeare').
parent_of('Thomas II Quiney', 'Thomas Quiney').
parent_of('Thomas II Quiney', 'Judith shakespeare').

% rules
% TODO add anscestor of
sibling_of(X,S):-parent_of(X,P),parent_of(S,P),X\==S.

brother_of(X,B):-sibling_of(X,B),male(B).

sister_of(X,S):-sibling_of(X,S),female(S).

mother_of(X,M):-parent_of(X,M),female(M).

father_of(X,M):-parent_of(X,M),male(M).

gp_of(X,GP):-parent_of(X,P),parent_of(P,GP).

ancestor_of(X, A):-parent_of(X, A) ; parent_of(X, P) , ancestor_of(P, A).

cousin_of(X,C):-
  gp_of(X,GP),
  gp_of(C,GP),
  X\==C,
  not(sibling_of(X,C)).
  
uncle_or_aunt_of(X,Who):-
  parent_of(X,P),
  sibling_of(P,Who).
  
uncle_of(X,Who):-uncle_or_aunt_of(X,Who),male(Who).

aunt_of(X,Who):-uncle_or_aunt_of(X,Who),female(Who).


  