from collections import namedtuple
n = int(input())
avg = 0
sum = 0
for i in range(n):
    Student = namedtuple('Student', 'ID MARKS NAME CLASS')
    ch = input().split()
    Student.ID = ch[0]
    Student.MARKS = ch[1]
    Student.NAME = ch[2]
    Student.CLASS =ch[3]
    sum = sum + int(Student.MARKS,10)

avg = sum/n
print(avg)
