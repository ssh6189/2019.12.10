def calc(a, b, op):
    if op == "+":
        return a+b
    elif op == "-":
        return a-b
    elif op == "*":
        return a*b
    elif op == "/":
        return a/b
    else:
        return print("올바르지 않은 입력값입니다....")

if __name__ == "__main__":
    x = int(input("수를 입력하시오."))
    z = str(input("연산자를 입력하시오."))
    y = int(input("수를 입력하시오."))

    print("결과 : ", calc(x, y, z))
