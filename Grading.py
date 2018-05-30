def gradingStudents(grades):
    y=[]
    for i in range(len(grades)):
        if grades[i] < 38 :
            y.append(grades[i])
        elif 5-grades[i] % 5 < 3 :
            x = 5-grades[i] % 5 + grades[i]
            y.append(x)
        else: y.append(grades[i])
    return y
gradingStudents([73,67,38,33])
print(gradingStudents([73,67,38,33]))