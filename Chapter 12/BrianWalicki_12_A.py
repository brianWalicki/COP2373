# This program takes a student grade csv file and outputs statistics

import numpy as np

# Counter for the number of passing students
counter = 0
# Total of all passing scores
score_passing = 0
# Opens the csv file for use in the program
csv = open("grades.csv")
csv_arr = np.genfromtxt("grades.csv", delimiter=",",
                        dtype=None)

# Creates an int array of just the grades
section = csv_arr[1:, 2:].astype(int)

# Create and use a mask to find passing scores
mask = section >= 60
passing_scores = section[mask]
# Calculates total score from all passed tests
for score in passing_scores:
    score_passing+=score

# Define functions to use in list comprehension below
stats_funcs = [np.mean, np.median, np.std, np.min, np.max]
stat_names = ['mean', 'median', 'std', 'min', 'max']

# Calculate overall statistics
overall_stats = [func(section) for func in stats_funcs]

# Calculate column statistics
col_stats = np.array([func(section, axis=0) for func in stats_funcs])

# Print overall statistics
for stat, value in zip(stat_names, overall_stats):
    print(f'Overall {stat}: {value}')

# Print column statistics
for i in range(3):
    for stat, value in zip(stat_names, col_stats[:, i]):
        print(f'Exam {i + 1} {stat}: {value}')

# Finds the number of passing students
for row in section:
    if np.mean(row) >= 60:
        counter += 1

# Prints how many have passed, and the average of the passed tests
print(f'{counter} students have passed with an average score of '
    f'{score_passing/counter/3} across all exams')
