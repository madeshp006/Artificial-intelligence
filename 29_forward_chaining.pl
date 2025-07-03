% Forward Chaining
% Facts
fact(sunny).
fact(warm).

% Rules
rule(go_beach) :- sunny, warm.
rule(take_umbrella) :- rainy.
rule(wear_coat) :- cold.

% Forward chaining engine
forward_chain(Goal) :-
    fact(Goal).

forward_chain(Goal) :-
    rule(Goal),
    call(Goal).

% Add new facts
add_fact(Fact) :-
    assert(fact(Fact)).
