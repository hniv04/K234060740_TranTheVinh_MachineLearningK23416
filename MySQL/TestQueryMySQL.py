# Lập trình Python kết nối MySQL Server

import mysql.connector

server = "localhost"
port = 3306
database = "studentmanagement"
username = "root"
password = "tuctung88"

conn = mysql.connector.connect(
                host = server,
                port = port,
                database = database,
                user = username,
                password = password)


# Truy vấn toàn bộ sinh viên

cursor = conn.cursor()

sql = "SELECT * FROM student"
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print("Truy vấn toàn bộ sinh viên:")
print(align.format('ID', 'Code', 'Name', "Age"))
for item in dataset:
    id = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(id, code, name, age))

cursor.close()


# Truy vấn sinh viên có độ tuổi từ 22 tới 26

cursor = conn.cursor()

sql = "SELECT * FROM student WHERE Age >= 22 AND Age <= 26"
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print("-" * 15)
print("Truy vấn sinh viên có độ tuổi từ 22 tới 26:")
print(align.format('ID', 'Code', 'Name', "Age"))
for item in dataset:
    id = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(id, code, name, age))

cursor.close()


# Truy vấn toàn bộ sinh viên và sắp xếp theo tuổi tăng dần

cursor = conn.cursor()

sql = "SELECT * FROM student ORDER BY Age ASC"
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print("-" * 15)
print("Truy vấn toàn bộ sinh viên và sắp xếp theo tuổi tăng dần:")
print(align.format('ID', 'Code', 'Name', "Age"))
for item in dataset:
    id = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(id, code, name, age))

cursor.close()


# Truy vấn sinh viên có độ tuổi từ 22 tới 26 và sắp xếp theo tuổi giảm dần

cursor = conn.cursor()

sql = "SELECT * FROM student WHERE Age >= 22 AND Age <= 26 ORDER BY Age DESC"
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print("-" * 15)
print("Truy vấn sinh viên có độ tuổi từ 22 tới 26 và sắp xếp theo tuổi giảm dần:")
print(align.format('ID', 'Code', 'Name', "Age"))
for item in dataset:
    id = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(id, code, name, age))

cursor.close()


# Truy vấn chi tiết thông tin sinh viên khi biết Id

cursor = conn.cursor()

sql = "SELECT * FROM student WHERE Id = 1"
cursor.execute(sql)

dataset = cursor.fetchone()
print("-" * 15)
print("Truy vấn chi tiết thông tin sinh viên khi biết Id:")
if dataset != None:
    id, code, name, age, avatar, intro = dataset
    print("Id = ", id)
    print("Code = ", code)
    print("Name = ", name)
    print("Age = ", age)

cursor.close()


# Truy vấn dạng phân trang 3 dòng đầu Student

cursor = conn.cursor()
sql = "SELECT * FROM student LIMIT 3 OFFSET 0"
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print("-" * 15)
print("Truy vấn dạng phân trang 3 dòng đầu Student:")
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(id, code, name, age))

cursor.close()


# Truy vấn dạng phân trang 3 dòng sau Student

cursor = conn.cursor()
sql = "SELECT * FROM student LIMIT 3 OFFSET 3"
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print("-" * 15)
print("Truy vấn dạng phân trang 3 dòng sau Student:")
print(align.format('ID', 'Code','Name',"Age"))
for item in dataset:
    id = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(id, code, name, age))

cursor.close()


# Truy vấn Paging toàn bộ dữ liệu theo N dòng

print("-" * 15)
print("PAGING!!!!!")
print("Truy vấn Paging toàn bộ dữ liệu theo N dòng:")
cursor = conn.cursor()
sql = "SELECT count(*) FROM student"
cursor.execute(sql)
dataset = cursor.fetchone()
rowcount = dataset[0]

limit = 3
step = 3
for offset in range(0, rowcount, step):
    sql = f"SELECT * FROM student LIMIT {limit} OFFSET {offset}"
    cursor.execute(sql)

    dataset=cursor.fetchall()
    align = '{0:<3} {1:<6} {2:<15} {3:<10}'
    print(align.format('ID', 'Code','Name',"Age"))
    for item in dataset:
        id = item[0]
        code = item[1]
        name = item[2]
        age = item[3]
        avatar = item[4]
        intro = item[5]
        print(align.format(id, code, name, age))

cursor.close()


# Thêm mới 1 Student

cursor = conn.cursor()

sql = "insert into student (code, name, age) values (%s, %s, %s)"

val = ("sv07", "Trần Duy Thanh", 45)

cursor.execute(sql, val)

conn.commit()

print("-" * 15)
print("Thêm mới 1 Student:")
print(cursor.rowcount, " record inserted")

cursor.close()


# Thêm mới nhiều Student

cursor = conn.cursor()

sql = "insert into student (code, name, age) values (%s, %s, %s)"

val = [
    ("sv08", "Trần Quyết Chiến", 19),
    ("sv09", "Hồ Thắng", 22),
    ("sv10", "Hoàng Hà", 25),
     ]

cursor.executemany(sql, val)

conn.commit()

print("-" * 15)
print("Thêm mới nhiều Student:")
print(cursor.rowcount, " record inserted")

cursor.close()


# Cập nhật tên Sinh viên có Code = ’sv09′ thành tên mới “Hoàng Lão Tà”

cursor = conn.cursor()
sql = "UPDATE student SET name = 'Hoàng Lão Tà' WHERE Code = 'sv09'"
cursor.execute(sql)

conn.commit()

print("-" * 15)
print("Cập nhật tên Sinh viên có Code = ’sv09′ thành tên mới “Hoàng Lão Tà”:")
print(cursor.rowcount, " record(s) affected")


# Cập nhật tên Sinh viên có Code = ’sv09′ thành tên mới “Hoàng Lão Tà” như viết dạng SQL Injection

cursor = conn.cursor()
sql = "UPDATE student SET name = %s WHERE Code = %s"
val = ('Hoàng Lão Tà', 'sv09')

cursor.execute(sql, val)

conn.commit()

print("-" * 15)
print("Cập nhật tên Sinh viên có Code = ’sv09′ thành tên mới “Hoàng Lão Tà” như viết dạng SQL Injection:")
print(cursor.rowcount, " record(s) affected")


# Xóa Student có ID = 14

cursor = conn.cursor()
sql = "DELETE FROM student WHERE ID = 14"
cursor.execute(sql)

conn.commit()

print("-" * 15)
print("Xóa Student có ID = 14:")
print(cursor.rowcount, " record(s) affected")


# Xóa Student có ID = 13 với SQL Injection

cursor = conn.cursor()
sql = "DELETE FROM student WHERE ID = %s"
val = (13, )

cursor.execute(sql, val)

conn.commit()

print("-" * 15)
print("Xóa Student có ID = 13 với SQL Injection:")
print(cursor.rowcount, " record(s) affected")


# Để xem lại có chuẩn xác hay không, cần truy vấn toàn bộ sinh viên để check

# Truy vấn toàn bộ sinh viên

cursor = conn.cursor()

sql = "SELECT * FROM student"
cursor.execute(sql)

dataset = cursor.fetchall()
align = '{0:<3} {1:<6} {2:<15} {3:<10}'
print("-" * 15)
print("Truy vấn toàn bộ sinh viên:")
print(align.format('ID', 'Code', 'Name', "Age"))
for item in dataset:
    id = item[0]
    code = item[1]
    name = item[2]
    age = item[3]
    avatar = item[4]
    intro = item[5]
    print(align.format(id, code, name, age))

cursor.close()