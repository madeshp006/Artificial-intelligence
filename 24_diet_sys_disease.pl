% Diet System based on Disease
disease(diabetes).
disease(hypertension).
disease(obesity).

diet_recommendation(diabetes, low_sugar).
diet_recommendation(diabetes, high_fiber).
diet_recommendation(hypertension, low_sodium).
diet_recommendation(hypertension, dash_diet).
diet_recommendation(obesity, low_calorie).
diet_recommendation(obesity, high_protein).

% Get diet advice
diet_advice(Disease, Diet) :-
    disease(Disease),
    diet_recommendation(Disease, Diet).
