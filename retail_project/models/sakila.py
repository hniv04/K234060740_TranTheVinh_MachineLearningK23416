from flask import Flask, request, render_template_string
from flaskext.mysql import MySQL
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from sklearn.cluster import KMeans
import numpy as np
app = Flask(__name__)
mysql = MySQL()

def getConnect(server, port, database, username, password):
    try:
        mysql = MySQL()
        # MySQL configurations
        app.config['MYSQL_DATABASE_HOST'] = server
        app.config['MYSQL_DATABASE_PORT'] = port
        app.config['MYSQL_DATABASE_DB'] = database
        app.config['MYSQL_DATABASE_USER'] = username
        app.config['MYSQL_DATABASE_PASSWORD'] = password
        mysql.init_app(app)
        conn = mysql.connect()
        return conn
    except mysql.connector.Error as e:
        print("Error = ", e)
    return None

def closeConnection(conn):
    if conn != None:
        conn.close()

def queryDataset(conn, sql, params=None):
    cur = conn.cursor()
    cur.execute(sql, params or ())
    rows = cur.fetchall()
    cols = [d[0] for d in cur.description]
    return pd.DataFrame(rows, columns=cols)

conn = getConnect('localhost', 3306, 'sakila', 'root', 'tuctung88')

def getCustomersByFilm(conn):
    sql = """
        SELECT f.title AS FilmTitle, c.customer_id, c.first_name, c.last_name
        FROM customer c
        JOIN rental r ON c.customer_id = r.customer_id
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        ORDER BY f.title, c.customer_id
    """
    df = queryDataset(conn, sql)
    df.columns = ['Film Title', 'Customer ID', 'First Name', 'Last Name']
    return df.drop_duplicates()

print("Phân loại khách hàng theo Tên phim:")
df_film_all = getCustomersByFilm(conn)
print(df_film_all)

def getCustomersByCategory(conn):
    sql = """
        SELECT cat.name AS CategoryName, c.customer_id, c.first_name, c.last_name
        FROM customer c
        JOIN rental r ON c.customer_id = r.customer_id
        JOIN inventory i ON r.inventory_id = i.inventory_id
        JOIN film f ON i.film_id = f.film_id
        JOIN film_category fc ON f.film_id = fc.film_id
        JOIN category cat ON fc.category_id = cat.category_id
        ORDER BY cat.name, c.customer_id
    """
    df = queryDataset(conn, sql)
    df.columns = ['Category Name', 'Customer ID', 'First Name', 'Last Name']
    return df.drop_duplicates()

print("=" * 10)
print("Phân loại khách hàng theo category:")
df_cat_all = getCustomersByCategory(conn)
print(df_cat_all)

# Lấy dữ liệu và gom cụm K_Means
def getClusteredData():
    sql = """
        SELECT 
            customer_id,
            COUNT(payment_id) AS total_payments,
            SUM(amount) AS total_amount,
            AVG(amount) AS avg_amount
        FROM payment
        GROUP BY customer_id
    """
    df = queryDataset(conn, sql)
    df.columns = ['CustomerID', 'Total Payments', 'Total Amount', 'Average Amount']

    X = df[['Total Payments', 'Total Amount', 'Average Amount']].values
    model = KMeans(n_clusters=4, init='k-means++', max_iter=500, random_state=42)
    df['cluster'] = model.fit_predict(X)
    return df

# Giao diện HTML đơn giản
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Phân cụm khách hàng theo Payment</title>
</head>
<body>
    <h2>Chọn cụm khách hàng để xem</h2>
    {% for i in range(4) %}
        <form method="get" action="/">
            <input type="hidden" name="cluster" value="{{ i }}">
            <button type="submit">Cụm {{ i }}</button>
        </form>
    {% endfor %}
    {% if customers %}
        <h3>Danh sách khách hàng thuộc cụm {{ selected_cluster }}</h3>
        <table border="1">
            <tr>
                <th>CustomerID</th>
                <th>Total Payments</th>
                <th>Total Amount</th>
                <th>Average Amount</th>
            </tr>
            {% for row in customers %}
            <tr>
                <td>{{ row['CustomerID'] }}</td>
                <td>{{ row['Total Payments'] }}</td>
                <td>{{ row['Total Amount'] }}</td>
                <td>{{ row['Average Amount'] }}</td>
            </tr>
            {% endfor %}
        </table>
    {% endif %}
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    cluster_id = request.args.get('cluster')
    df = getClusteredData()
    customers = None
    selected_cluster = None
    if cluster_id is not None:
        cluster_id = int(cluster_id)
        selected_cluster = cluster_id
        customers = df[df['cluster'] == cluster_id].to_dict(orient='records')
    return render_template_string(HTML_TEMPLATE, customers=customers, selected_cluster=selected_cluster)

if __name__ == '__main__':
    app.run(debug=True)