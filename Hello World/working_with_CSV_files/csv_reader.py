import csv

# with open('cars.csv') as file:
#     csv_reader = csv.reader(file)
#     next(csv_reader)
#     for car in csv_reader:
#         # print(car)
#         print(f'{car[1]} {car[2]} costs {car[4]}')


with open('cars.csv') as file:
    csv_reader = csv.reader(file)
    data_list = list(csv_reader)
    print(data_list)