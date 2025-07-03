% Bird flight program
bird(sparrow).
bird(eagle).
bird(penguin).
bird(ostrich).

can_fly(X) :- bird(X), \+ flightless(X).

flightless(penguin).
flightless(ostrich).

% Query birds that can fly
flying_bird(X) :- can_fly(X).
