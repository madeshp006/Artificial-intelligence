% Best First Search
node(a, 5).
node(b, 3).
node(c, 4).
node(d, 2).
node(e, 0).

edge(a, b, 2).
edge(a, c, 3).
edge(b, d, 1).
edge(c, e, 2).
edge(d, e, 1).

% Heuristic function
h(Node, H) :- node(Node, H).

% Best first search
best_first_search(Start, Goal, Path) :-
    best_first([[Start]], Goal, Path).

best_first([Path|_], Goal, Path) :-
    Path = [Goal|_].

best_first([Path|Paths], Goal, Solution) :-
    extend_path(Path, NewPaths),
    append(Paths, NewPaths, AllPaths),
    sort_paths(AllPaths, SortedPaths),
    best_first(SortedPaths, Goal, Solution).
