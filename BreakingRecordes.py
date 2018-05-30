def breakingrecords (score):
    x = score[0]
    y = score[0]
    max = 0
    min =0
    z = []
    for i in range(len(score)):

        if x < score[i]:
            x = score[i]
            max = max +1
        elif y > score[i]:
            y = score[i]
            min = min+ 1
    z.append(max)
    z.append(min)
    return z

print(breakingrecords([10,5,20,20,4,5,2,25,1]))