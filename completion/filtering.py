from numpy import nan as NA
import pandas as pd

data = pd.DataFrame([[1., 6.5, 3.],
                     [1., NA, NA],
                     [NA, NA, NA],
                     [-1, -5, -3],
                     [NA, 6.5, 3.]])
print("Data ban đầu:")
print(data)
print("-" * 10)

cleaned = data.dropna()
print("Data bỏ dòng chứa NA:")
print(cleaned)
print("-" * 10)

cleaned2 = data.dropna(how = 'all')     # Xóa dòng nào chứa tất tần tật NA
print("Data bỏ dòng toàn NA:")
print(cleaned2)
print("-" * 10)

cleaned3 = data[(data >= 0).all(axis=1)]
print("Data bỏ dòng toàn âm:")
print(cleaned3)
