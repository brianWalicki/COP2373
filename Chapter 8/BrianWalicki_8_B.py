# Reads data from a csv and prints it using f-string

import csv

def read_csv(filename):
    data = []

    # Reads specified file
    with open (filename, 'r') as file:
        reader = csv.reader(file)

        # Appends rows from csv file to data[] in this format for each student
        # [firstName,lastName,Grade1,Grade2,Grade3]
        for row in reader:
            data.append([row[0], row[1]] + [value for value in row[2:]])
        for row in data:
            print(f"{row[0]:<12}{row[1]:<12}{row[2]:<7}{row[3]:<7}{row[4]:<7}")

read_csv('grades.csv')