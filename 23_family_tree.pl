% Family Tree
parent(tom, bob).
parent(pam, bob).
parent(bob, ann).
parent(bob, pat).
parent(pat, jim).

male(tom).
male(bob).
male(jim).
female(pam).
female(ann).
female(pat).

% Family relationships
father(X, Y) :- parent(X, Y), male(X).
mother(X, Y) :- parent(X, Y), female(X).
sibling(X, Y) :- parent(Z, X), parent(Z, Y), X \= Y.
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
