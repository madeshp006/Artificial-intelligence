% Pattern Matching in Prolog
% Simple pattern matching
match_pattern([], []).
match_pattern([H|T1], [H|T2]) :- 
    match_pattern(T1, T2).

% Wildcard pattern matching
match_wildcard([], []).
match_wildcard([_|T1], [_|T2]) :- 
    match_wildcard(T1, T2).

% Pattern with specific values
match_specific([X, Y, Z], [1, 2, 3]) :-
    X = 1, Y = 2, Z = 3.

% Variable binding in patterns
extract_pattern([First, Second|Rest], First, Second, Rest).
