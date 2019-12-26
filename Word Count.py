f = open("c:/Users/yesterday.txt",'r')

result = 0

for i in range(40):
    yl = f.readline()
    yl = yl.title()

    print(yl)
    

    if(yl.count("Yesterday")):
        result = result + 1


print(result)
