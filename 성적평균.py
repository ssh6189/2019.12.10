score = [[49, 80, 20, 100, 80], [43, 60, 85, 30, 90], [49, 82, 48, 50, 100]]

s = [0, 0, 0, 0,0]



for i in range(3):
    for j in range(5):
        s[i] = s[i] + score[j][i]
        j = j + 1
    i = i + 1

i = 0
while(i<5):
    print(s[i])
    i = i + 1

str(input())
