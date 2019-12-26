for num in range(1, 10) :  # 1~9
    for dan in range(2, 10) : #2~9        
        gugu = "{0} X {1}={2:2d} ".format(dan, num, (num*dan))   #3버전부터 지원
        print(gugu , end=" ")           
    print()
#%operator 를 지원하지만 공식문서에서는 권장하지 않는다고 합니다.    
    
for num in range(1, 10) :  # 1~9
    for dan in range(2, 10) : #2~9
        f = f'{dan}X{num}={num*dan} '  #3.6버전 f-string
        print(f, end=" ")          
    print()
#%operator 를 지원하지만 공식문서에서는 권장하지 않는다고 합니다. 
