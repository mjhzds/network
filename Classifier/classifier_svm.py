import numpy as np
from sklearn.model_selection import GridSearchCV, train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import joblib

def svm(x_train, x_test, y_train, y_test):
    # rbf核函数，设置数据权重
    svc = SVC(kernel='rbf', class_weight='balanced')
    c_range = np.logspace(-5, 15, 11, base=2)
    gamma_range = np.logspace(-9, 3, 13, base=2)
    # 网格搜索交叉验证的参数范围，cv=3,3折交叉
    param_grid = [{'kernel': ['rbf'], 'C': c_range, 'gamma': gamma_range}]
    grid = GridSearchCV(svc, param_grid, cv=3, n_jobs=-1)
    # 训练模型
    clf = grid.fit(x_train, y_train)
    # 计算测试集精度
    score = grid.score(x_test, y_test)
    print('精度为%s' % score)
    joblib.dump(grid, 'svm.pkl')

def load_data():
    p = r'G:\pythonwork\network\result.csv'
    with open(p, encoding='utf-8') as f:
        data = np.loadtxt(f, str, delimiter=",", skiprows=1)
        x = data[:, 0:-2]
        y = data[:, -1]
        scaler = StandardScaler()
        x_std = scaler.fit_transform(x)  # 标准化
        x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=.3)
    return x_train, x_test, y_train, y_test

if __name__ == '__main__':
    svm(*load_data())

