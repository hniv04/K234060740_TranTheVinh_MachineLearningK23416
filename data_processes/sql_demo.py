import sqlite3
import pandas as pd

try:
    # Connect to DB and create a cursor
    sqliteConnection = sqlite3.connect('../databases/Chinook_Sqlite.sqlite')
    cursor = sqliteConnection.cursor()
    print('DB Init')

    # Write a query and execute it with cursor
    query = 'SELECT * FROM InvoiceLine LIMIT 5'
    cursor.execute(query)

    # Fetch and output result with column names
    cols = [desc[0] for desc in cursor.description]   # lấy tên cột
    df = pd.DataFrame(cursor.fetchall(), columns=cols)
    print(df)

    # CLose the cursor
    cursor.close()

# Handle errors
except sqlite3.Error as error:
    print('Error: %s' % error)

# Close DB Connection irrespective of success or failure
finally:
    if sqliteConnection:
        sqliteConnection.close()
        print('sqlite connection closed')
