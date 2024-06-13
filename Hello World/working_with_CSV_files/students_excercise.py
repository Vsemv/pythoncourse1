import csv
import os


def add_student(name, surname, age):
    
    file_exists = os.path.isfile('students.csv')
    
    with open('students.csv', 'a', newline='') as file:
        csv_writer = csv.writer(file)
        if not file_exists:
            csv_writer.writerow(['Name', 'Surname', 'Age'])
        csv_writer.writerow([name, surname, age])
        

# add_student('Corey', 'Taylor', 45)


def print_students():
    
    with open('students.csv') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for student in csv_reader:
            print(student)
            
print_students()