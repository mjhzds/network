import pandas as pd
import numpy as np
from sklearn import cluster
from Classifier.classifier_svm import svm
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler


def value_count(df):
    columns = df.columns.tolist()
    for c in columns:
        d = df[c]
        print(d.value_counts())

def load_data(x, y):
    scaler = StandardScaler()
    x_std = scaler.fit_transform(x)  # 标准化
    # 将数据划分为训练集和测试集，test_size=.3表示30%的测试集
    x_train, x_test, y_train, y_test = train_test_split(x_std, y, test_size=.3)
    return x_train, x_test, y_train, y_test

if __name__ == '__main__':
    data = pd.read_csv("middata.csv")
    # rowdata = pd.read_csv("event_utf8.csv")
    data.columns = ["index", '事件等级', '事件类型', '设备IP地址', '设备类型', '源IP地址', '目的IP地址', '源端口', '目的端口', '响应', '事件原始内容']
    # rowdata.columns = ["事件接收时间","事件等级","事件类型","设备IP地址","设备类型","源IP地址","目的IP地址","源端口","目的端口","响应","设备名称","事件原始内容"]
    data.dropna(axis=1, inplace=True)
    # rowdata.dropna(axis=0, inplace=True)
    data.drop(columns="index", inplace=True)
    eps, min_samples = 0.15, 40
    dbscan = cluster.DBSCAN(eps=eps, min_samples=min_samples)
    # 模型拟合
    dbscan.fit(data)
    data["cluster"] = dbscan.labels_

    # print(type(rowdata))
    # rowdata["cluster"] = dbscan.labels_
    # rowdata.to_csv("labels.csv")

