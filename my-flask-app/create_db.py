import sqlite3

# 连接到SQLite数据库（如果数据库不存在，则会自动创建）
conn = sqlite3.connect('database.db')

# 创建一个游标对象
cursor = conn.cursor()

# 创建用户表
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
)
''')

# 提交更改并关闭连接
conn.commit()
conn.close()
