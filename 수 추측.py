import random
import time
import os

n = -1
answer = random.randrange(1, 100)
life = 4

while ((n != answer)):

    os.system('cls')
    print("life : ", life+1)
    n = int(input("추측하는 수를 입력하시오."))

    if (life > 0):
        if (answer > n):
            print("더 큰 수를 입력하시오.")
            time.sleep(1)
            life = life - 1
            

        elif (answer < n):
            print("더 작은 수를 입력하시오.")
            life = life - 1
            time.sleep(1)
            

        else:
            print("정답입니다!")
            break

    else:
        print("라이프가 모두 소진되었습니다. 당신의 패배입니다.")
        break
    
str(input())
    
