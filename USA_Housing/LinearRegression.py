# Bước 1: Import thư viện cần thiê

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Bước 2: Tải và xem thông tin dữ lệu csv

df = pd.read_csv('USA_Housing.csv')
print(df.head())
print("=" * 10)

print(df.info())
print("=" * 10)

print(df.describe())
print("=" * 10)

numeric_df = df.select_dtypes(include=[np.number])
sns.heatmap(numeric_df.corr(), annot = True, cmap = 'coolwarm')
plt.show()

# Bước 3: Xây dựng và train mô hình dự báo

X = df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms','Avg. Area Number of Bedrooms', 'Area Population']]
y = df['Price']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)

# Bước 4: Sử dụng mô hình

predictions = lm.predict(X_test)

pre1 = lm.predict([X_test.iloc[0]])
print("kết quả =",pre1)
print("=" * 10)

pre2 = lm.predict([[66774.995817,5.717143, 7.795215, 4.320000, 36788.980327]])
print("kết quả 2 =",pre2)
print("=" * 10)

# Bước 5: Đánh giá mô hiình

print(lm.intercept_)
coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
print(coeff_df)
print("=" * 10)

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
print("=" * 10)

# Bước 6: Kết xuâ mô hình ra file zip

import pickle
modelname = "housingmodel.zip"
pickle.dump(lm, open(modelname, 'wb'))

modelname = "housingmodel.zip"
trainedmodel = pickle.load(open(modelname, 'rb'))

features = pd.Index(['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms', 'Avg. Area Number of Bedrooms', 'Area Population'], dtype='object')
coeff_df = pd.DataFrame(trainedmodel.coef_, features,columns=['Coefficient'])
print(coeff_df)
print("=" * 10)

prediction = trainedmodel.predict([[66774.995817,5.717143,7.795215,4.320000,36788.980327]])
print("Kết quả =", prediction)