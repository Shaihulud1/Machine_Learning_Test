from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

iris_dataset = load_iris()

#print(iris_dataset.keys())
# dict_keys(['data', 'target', 'target_names', 'DESCR', 'feature_names'])
#['setosa' 'versicolor' 'virginica']

#print(iris_dataset['data'])
#print(iris_dataset['data'])

X_train, X_test, y_train, y_test = train_test_split(
    iris_dataset['data'], iris_dataset['target'], random_state=0)

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)

X_randomTest = np.array([[5, 2.9, 1, 0.2]])
prediction = knn.predict(X_randomTest)

arPredict = knn.predict(X_test)

print(str(knn.score(X_test, y_test))) #SCORE 97%

print(prediction)
print(iris_dataset['target_names'][prediction])
#print(y_test)
