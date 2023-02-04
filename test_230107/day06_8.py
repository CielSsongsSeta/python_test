<<<<<<< HEAD
# 머신러닝용
# pip install scikit-learn

import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print(sklearn.__version__)

운동시간 = [[1],[2],[3],[4],[5]]
근육량 = [[1],[2],[3],[3.5],[3.7]]

lin = LinearRegression()

lin.fit(운동시간, 근육량)

근육량예측 = lin.predict(운동시간)
print(근육량예측)
print('2.5시간 운동하면 근육 증가량은',lin.predict([[2.5]]),'입니다.')

plt.plot(운동시간, 근육량, color='blue')
plt.scatter(운동시간, 근육량예측, color='green')
=======
# 머신러닝용
# pip install scikit-learn

import sklearn
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

print(sklearn.__version__)

운동시간 = [[1],[2],[3],[4],[5]]
근육량 = [[1],[2],[3],[3.5],[3.7]]

lin = LinearRegression()

lin.fit(운동시간, 근육량)

근육량예측 = lin.predict(운동시간)
print(근육량예측)
print('2.5시간 운동하면 근육 증가량은',lin.predict([[2.5]]),'입니다.')

plt.plot(운동시간, 근육량, color='blue')
plt.scatter(운동시간, 근육량예측, color='green')
>>>>>>> 7dfafd19baae55259413a3bfdab76f37fce25b06
plt.show()