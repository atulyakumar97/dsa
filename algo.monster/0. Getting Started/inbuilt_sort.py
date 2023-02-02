from functools import cmp_to_key

# task tuples (description, priority)
tasks = [
    ('Cook dinner', 5),
    ('Buy grocery', 3)
]

# sort tasks by priority in ascending order
sorted_tasks = sorted(tasks, key=lambda task: task[1])
print(sorted_tasks)

arr = [
    ('Cook dinner', 5),
    ('Buy grocery', 3),
    ('Repair Fridge', 1)
]


# or use cmp_to_key ????????????????????????????????????????????????
sorted_tasks = sorted(arr, key=cmp_to_key(lambda t1, t2: t1[1] - t2[1]))
print(sorted_tasks)

# sorting using inbuilt functions of objects #


class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_marks(self):
        return self.marks

    def get_name(self):
        return self.name


student_list = [Student('s1', 100),
                Student('s2', 45),
                Student('s3', 90)]

student_list.sort(key=lambda s: s.get_marks())

for student in student_list:
    print(student.get_name(), student.get_marks())
