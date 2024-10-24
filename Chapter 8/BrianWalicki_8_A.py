# This program asks for information from the user and formats it into a csv

import csv

# get_info() asks for information then returns it for use later
# it also formats the data slightly by adding a new line after the names
def get_info():
    grades = []
    names = []
    num_students = int(input('How many students? '))

    # Asks for first/last names and appends to names[]
    for i in range(num_students):
        names.append(str(input('First name? ')))
        names.append(str(input('Last name? ')))
        names.append("\n")

        # Asks for grades and appends to grades[]
        for j in range(3):
            grade = int(input(f"{j + 1}st exam grade? "))
            grades.append(grade)

    # Returns the data as a tuple
    return grades, names, num_students

#Creates a csv file by using the data from get_info()
def make_csv(info):

    # Unpacks the tuple for use in the loop
    grades, names, num_students = info

    # Either creates or opens 'grades.csv' in write mode
    with open('grades.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        header = ('First Name' , 'Last Name' , 'Exam 1' ,
                        'Exam 2' , 'Exam 3')
        writer.writerow(header)
        # Fills the csv with data in this format for each student
        # firstName, lastName, Grade1, Grade2, Grade3
        for i in range(num_students):
            writer.writerow(names[i * 3:(2 + 3 * i)] + grades[i * 3:(3 + 3 * i)])

make_csv(get_info())
