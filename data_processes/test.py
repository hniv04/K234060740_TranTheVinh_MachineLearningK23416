import pandas as pd

# Đọc file CSV
df = pd.read_csv('../dataset/SalesTransactions.csv')

# Tạo cột doanh thu
df['Revenue'] = df['UnitPrice'] * df['Quantity'] * (1 - df['Discount'])

top_revenue = (
    df.groupby("ProductID")["Revenue"]
      .sum()
      .sort_values(ascending=False)
      .head(3)
)

print("Top 3 sản phẩm có doanh thu cao nhất:")
for pid, rev in top_revenue.items():
    print(f"- ProductID {pid}: {rev:.2f} VND")
