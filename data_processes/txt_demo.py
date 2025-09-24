import pandas as pd

df = pd.read_csv("..\dataset\SalesTransactions.txt",
                 encoding = 'utf-8', dtype = 'unicode',
                 sep = '\t',
                 low_memory = False)

# Dùng ..\ chứ không khai báo full ổ đia --> bị trừ điểm

"""
df = pd.read_csv("D:\TÀI LIỆU HỌC TẬP\HỌC MÁY TRONG PHÂN TÍCH KINH DOANH\ML_K23406\dataset\SalesTransactions.txt",
                 encoding = 'utf-8', dtype = 'unicode',
                 sep = '\t',
                 low_memory = False)
"""

print(df)
print("-" * 10)

# Chuyển cột về số
df['UnitPrice'] = pd.to_numeric(df['UnitPrice'], errors='coerce')
df['Quantity'] = pd.to_numeric(df['Quantity'], errors='coerce')
df['Discount'] = pd.to_numeric(df['Discount'], errors='coerce')

# Tạo cột Price = UnitPrice * Quantity (áp dụng chiết khấu nếu muốn)
df['Price'] = df['UnitPrice'] * df['Quantity'] * (1 - df['Discount'])

# Tính tổng doanh thu theo OrderID
revenue_by_product = df.groupby('OrderID', as_index=False)['Price'].sum()
print(revenue_by_product)
print("-" * 10)

# Top 3 sản phẩm có doanh thu cao nhất
top3_highest = revenue_by_product.sort_values(by='Price', ascending=False).head(3)
print(top3_highest)
print("-" * 10)

# Top 3 sản phẩm có doanh thu thấp nhất
top3_lowest = revenue_by_product.sort_values(by='Price', ascending=True).head(3)
print(top3_lowest)