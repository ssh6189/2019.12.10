decimal = 10
result = ''

while ((decimal > 10)):
    remainder = decimal %2
    decimal = decimal // 2
    result = str(remainder) + result
    
print(result)

str(input())
