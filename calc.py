def add(x, y):
    return x+y

if __name__ == '__main__':
    print(add(3, 5))

    
#__name__은 특별한 변수 이름
#calc.py를 직접 실행시키면 __name__변수에 __main__ 값이 저장됩니다.
#import되면 __name__변수에 calc.py값이 저장됩니다.
