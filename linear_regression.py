
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("Mansion1.csv")

# まずは量的変数のみの場合、係数の推定
predictor = ['大きさ']
response = ['家賃']
X = np.hstack((np.ones((df.shape[0],1)), np.array(df[predictor])))
y = np.array(df[response])

Xt = X.transpose()
coeff = np.dot(np.dot(np.linalg.inv(np.dot(Xt, X)), Xt), y)
prediction = np.dot(X, coeff)
error = y - prediction

plt.scatter(df[predictor], df[response])
x=np.linspace(df[predictor].min(axis=0)[0], df[predictor].max(axis=0)[0])
plt.plot(x, np.dot(np.hstack((np.ones((x.shape[0],1)), x.reshape(-1,1))), coeff)) # 回帰直線
plt.show()


# linear regression classを作る
# attributeはcoefficientsとintercept
# methodはfit, get_params, predict

class LinearRegression():
    def __init__(self):
        self.coefficients = None
        self.intercept = None
        self.df = None

    def fit(self, df, predictor, response):
        self.df = df
        X = np.hstack((np.ones((self.df.shape[0], 1)), np.array(self.df[predictor])))
        y = np.array(self.df[response])
        Xt = X.transpose()
        self.coefficients = np.dot(np.dot(np.linalg.inv(np.dot(Xt, X)), Xt), y)

    def get_params(self):
        return self.coefficients

    def predict(self, df, predictor, response):
        X = np.hstack((np.ones((self.df.shape[0], 1)), np.array(self.df[predictor])))
        y = np.array(self.df[response])
        return np.dot(X, self.coefficients)

    def Rsq(self, df, predictor, response):
        y = np.array(self.df[response])
        error = y - self.predict(df, predictor, response)
        return 1 - (sum(error ** 2)) / sum((y - np.mean(y)) ** 2)

x = LinearRegression()
x.fit(df, predictor, response)
print(x.get_params())
print(x.Rsq(df, predictor, response))

# ダミー変数の扱い
