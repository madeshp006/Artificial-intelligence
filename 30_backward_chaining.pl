% Backward Chaining
% Knowledge base
parent(tom, bob).
parent(bob, ann).
parent(bob, pat).

% Rules
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Backward chaining (automatic in Prolog)
prove(Goal) :- call(Goal).

% Trace the proof
trace_proof(Goal) :-
    write('Proving: '), write(Goal), nl,
    call(Goal),
    write('Proved: '), write(Goal), nl.
