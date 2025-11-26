

################################################# 1) Create stats of students marks 
"""
You must do:

Convert to NumPy array
Calculate:
mean
median
standard deviation
highest
lowest
Print results
BONUS: Normalize the marks:

"""

import numpy as np

arr = [65, 70, 85, 90, 75, 60, 80]
marks = np.array(arr)

mean = marks.mean()
median = np.median(marks)
std_value = marks.std()
max_value = marks.max()
min_value = marks.min()

normalized = (marks - min_value) / (max_value - min_value)

print(f"Mean: {mean}")
print(f"Median: {median}")
print(f"Standard Deviation: {std_value}")
print(f"Highest: {max_value}")
print(f"Lowest: {min_value}")
print(f"Normalized Marks: {normalized}")
