n = int(input())
names = []
grades = []
matrix = []
FinalNames = []
c=0
for i in range(0,n):
    for j in range(0,2):
        if j==0:
            name = input()
            matrix.append(name)
        else:
            grade = float(input())
            grades.append(grade)
            matrix.append(grade)

grades.sort()
for i in range(0,n):
    if grades[i]!=grades[0]:
        Second_Lowest = grades[i]
        break

for i in range(0,(n*2)):
    if i%2 != 0:
        if matrix[i] == Second_Lowest:
            FinalNames.append(matrix[i-1])
            c=c+1

FinalNames.sort()
for i in range(0,c):
    print(FinalNames[i])