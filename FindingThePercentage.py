if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

scoreList = student_marks[query_name]
sumScores = 0
for i in scoreList:
    sumScores+=i
averagePercent = sumScores/3
print('%.2f' % averagePercent)
