from sklearn.metrics import accuracy_score

from Classifier.classifier_svm import load_data
import sklearn.tree as st
import joblib
import sklearn.metrics as sm


def tree(x_train, x_test, y_train, y_test):
    model = st.DecisionTreeClassifier(max_depth=7)
    model.fit(x_train, y_train)
    pred_y = model.predict(x_test)
    accuracy_s = accuracy_score(y_test, pred_y)  # 准确率
    print(accuracy_s)
    joblib.dump(model, "tree.pkl")

if __name__ == '__main__':
    tree(*load_data())

