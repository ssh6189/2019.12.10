import time
import os

 n = int(input("구구단 몇단을(1~9)? 계산할까요?, 종료하고 싶으시면, 0을 입력하시오."))
 
while(n == 1):

    n = int(input("구구단 몇단을(1~9)? 계산할까요?, 종료하고 싶으시면, 0을 입력하시오."))

    print("구구단 n단을 계산합니다")

    for i in range(1, 10):
        print(n, "x", i, "=", n*i)

    time.sleep(5)
    os.system('cls')

print("프로그램을 종료합니다.")

    
