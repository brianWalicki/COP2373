# Reads data from a csv and prints it into multiple lists

import csv

def read_csv(filename):
    data = []

    # Reads specified file
    with open (filename, 'r') as file:
        reader = csv.reader(file)

        # Appends rows from csv file to data[] in this format for each student
        # [firstName,lastName,Grade1,Grade2,Grade3]
        for row in reader:
            data.append([row[0], row[1]] + [int(value) for value in row[2:]])
        return data

print(read_csv('grades.csv'))