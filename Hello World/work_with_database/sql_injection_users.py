import sqlite3
conn = sqlite3.connect("sqlite/sql_injection_users_db.db")

# create_query = "CREATE TABLE users (user_name TEXT, user_password TEXT)"

users = [
    ('jack123', 'regh45w'),
    ('janepretty444', 'w3rghwrj4'),
    ('bobman123', 'reyu67564er')
]

# insert_query = "INSERT INTO users VALUES (?, ?)"

user_name = input('Input your username ')
user_password = input('Input your password ')

#           not correct method:
# select_query = f"SELECT * FROM users WHERE user_name='{user_name}' AND user_password='{user_password}'"

#           correct method:
select_query = f"SELECT * FROM users WHERE user_name=? AND user_password=?"


cursor = conn.cursor()

cursor.execute(select_query, (user_name, user_password))
data = cursor.fetchone()
if(data):
    print('You are logged in!')
else:
    print('Please try again')
    

# cursor.executemany(insert_query, users)

conn.commit()

conn.close()