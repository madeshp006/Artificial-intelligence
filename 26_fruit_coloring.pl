% Fruit and Color with Backtracking
fruit_color(apple, red).
fruit_color(apple, green).
fruit_color(banana, yellow).
fruit_color(orange, orange).
fruit_color(grape, purple).
fruit_color(grape, green).

% Find all fruit colors
all_colors(Fruit, Color) :-
    fruit_color(Fruit, Color),
    fail.
all_colors(_, _).

% Find fruits of specific color
fruit_of_color(Color, Fruit) :-
    fruit_color(Fruit, Color).
