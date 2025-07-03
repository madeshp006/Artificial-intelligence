% Medical Diagnosis System
symptom(fever).
symptom(cough).
symptom(headache).
symptom(rash).
symptom(runny_nose).

% Disease diagnosis rules
disease(flu) :- 
    symptom(fever),
    symptom(cough),
    symptom(headache).

disease(cold) :-
    symptom(runny_nose),
    symptom(cough).

disease(measles) :-
    symptom(fever),
    symptom(rash),
    symptom(cough).

% Diagnosis
diagnose(Patient, Disease) :-
    write('Diagnosing '), write(Patient), nl,
    disease(Disease),
    write('Diagnosis: '), write(Disease), nl.
