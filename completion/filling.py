from numpy import nan as NA
import pandas as pd

# Dữ liệu ban đầu
data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [4, 7, 2],
                     [0.5, 8, NA],
                     [NA, 6.5, 3.]])
print("Dữ liệu gốc:")
print(data)
print("-" * 20)

# Điền bằng mean
filled_mean = data.fillna(data.mean())
print("Điền bằng mean:")
print(filled_mean)
print("-" * 20)

# Điền bằng median
filled_median = data.fillna(data.median())
print("Điền bằng median:")
print(filled_median)
print("-" * 20)

# Điền bằng mode (lấy mode đầu tiên)
filled_mode = data.fillna(data.mode().iloc[0])
print("Điền bằng mode:")
print(filled_mode)
