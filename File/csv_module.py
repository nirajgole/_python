# from csv import reader
# with open('E:\Gole_Niraj\Programming\P_Y_T_H_O_N\File\international-migration-December-2021-estimated-migration-by-age-sex.csv') as file:
#       #reader takes second argument as delimeter default comma
#     csv_reader = reader(file)
#     data = list(csv_reader)
#     print(data)

# from csv import DictReader
# with open('E:\Gole_Niraj\Programming\P_Y_T_H_O_N\File\international-migration-December-2021-estimated-migration-by-age-sex.csv') as file:
#     csv_reader = DictReader(file)
#     for row in csv_reader:
#         # each row will be orderDict
#         print(row['age'])

# write to CSV file
from csv import writer, reader
with open('cats.csv', 'w') as file:
    csv_writer = writer(file)
    csv_writer.writerow(['name', 'age'])
    csv_writer.writerow(['Garfield', '1'])
    csv_writer.writerow(['Heathcliff', '2'])
    csv_writer.writerow(['Josie', '3'])
