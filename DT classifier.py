from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
X = [
    [80, 85, 70],
    [60, 65, 55],
    [90, 90, 80],
    [30, 40, 35],
    [75, 70, 65],
    [50, 60, 45]
]

y = [1, 0, 1, 0, 1, 0]

model = DecisionTreeClassifier()
model.fit(X, y)

new_student = [[70, 75, 60]]
prediction = model.predict(new_student)

print("Prediction for new student (1 = Pass, 0 = Fail):", prediction[0])

tree.plot_tree(model, feature_names=["Attendance", "Assignments", "Past Grade"], class_names=["Fail", "Pass"], filled=True)
