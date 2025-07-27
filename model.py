from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

def load_model():
    iris = load_iris()
    X = pd.DataFrame(iris.data, columns=iris.feature_names)
    y = iris.target
    clf = RandomForestClassifier()
    clf.fit(X, y)
    return clf, iris.feature_names

def predict_class(clf, feature_names, input):
    df = pd.DataFrame([{
        feature_names[0]: input.sepal_length,
        feature_names[1]: input.sepal_width,
        feature_names[2]: input.petal_length,
        feature_names[3]: input.petal_width
    }])
    prediction = clf.predict(df)
    return int(prediction[0])
