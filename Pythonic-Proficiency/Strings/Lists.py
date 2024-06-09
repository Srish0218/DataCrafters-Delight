"""Jagged list A jagged list in Python is a list of lists, where the inner lists can be of different lengths. Jagged
lists are also known as ragged arrays or irregular arrays. Jagged lists are different from multidimensional arrays,
which are always rectangular. However, jagged arrays are often used to emulate multidimensional arrays. Jagged arrays
are supported in languages such as Java, PHP, Python (multidimensional lists), Ruby, C#.NET, Visual Basic.NET,
and Perl. Here is an example of a jagged list in Python: Python

jagged_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9]] This list contains three inner lists, with lengths 3, 2, and 4,
respectively. Jagged lists can be useful for representing data that is not naturally rectangular. For example,
you could use a jagged list to represent a list of students, where each student has a different number of grades.
Here is an example of how to use a jagged list to represent a list of students: Python

students = [["Alice", [90, 85, 95]], ["Bob", [80, 90, 75]], ["Carol", [95, 100, 90]]] This list contains three inner
lists, each of which represents a student. The first element of each inner list is the student's name, and the second
element is a list of the student's grades. Jagged lists can be more difficult to work with than multidimensional
arrays, but they can be useful for representing data that is not naturally rectangular."""