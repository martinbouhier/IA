from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
a = [[0, 1], [0, 0], [1, 1], [1, 0], [1, 1], [0, 0], [1, 1], [1, 0]]

b = [1, 0, 1, 0, 1, 0, 1, 0]

X_train, X_test, y_train, y_test = train_test_split(a, b)
knn = KNeighborsClassifier(n_neighbors=6)
knn.fit(X_train, y_train)
knn.score(X_train, y_train)
knn.predict([[0, 1]])
