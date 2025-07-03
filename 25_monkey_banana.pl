% Monkey Banana Problem
state(monkey_pos, box_pos, on_box, has_banana).

% Initial state
initial_state(state(door, window, floor, no)).

% Goal state
goal_state(state(_, _, _, yes)).

% Actions
action(state(Pos, Pos, floor, no), climb, 
       state(Pos, Pos, on_box, no)).

action(state(Pos1, Pos2, floor, no), push(Pos1, Pos3),
       state(Pos3, Pos3, floor, no)) :- 
       Pos1 \= Pos2.

action(state(middle, middle, on_box, no), grasp,
       state(middle, middle, on_box, yes)).

% Solve the problem
solve_monkey :- 
    initial_state(Start),
    goal_state(Goal),
    solve(Start, Goal, []).
