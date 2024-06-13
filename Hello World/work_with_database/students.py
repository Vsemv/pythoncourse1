import sqlite3
conn = sqlite3.connect("sqlite/students_db.db")

cursor = conn.cursor()
# cursor.execute("CREATE TABLE students (first_name TEXT, last_name TEXT, age INTEGER);")

# insert_query = "INSERT INTO students VALUES ('James', 'Brown', 21);"
# cursor.execute("INSERT INTO students VALUES ('James', 'Brown', 21);")
first_name = 'Jack'
last_name = 'White'
age = 22

jane = ('Jane', 'Air', 18)
students = [
    ('Jane', 'Ostin', 19),
    ('Jack', 'Scott', 22),
    ('Bob', 'Green', 20)
]

# Bad approach! SQL injection danger!
# insert_query = f"INSERT INTO students VALUES ('{first_name}', '{last_name}', {age});"

#Good approach!
insert_query = "INSERT INTO students VALUES (?,?,?);"

# cursor.execute(insert_query, (first_name, last_name, age))
# cursor.execute(insert_query, jane)

# for student in students:
#     cursor.execute(insert_query, student)

cursor.executemany(insert_query, students)

conn.commit()

conn.close()