#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(5)
student_grades = np.random.normal(68, 15, 50)

intervalos = [40, 50, 60, 70, 80, 90, 100]
plt.hist(x=student_grades, bins=intervalos, edgecolor='black', linewidth=1.2)
plt.axis([0, 100, 0, 30])
plt.xticks(range(0, 110, 10))
plt.xlabel('Grades')
plt.ylabel('Number of Students')
plt.title("Project A")
plt.show()
