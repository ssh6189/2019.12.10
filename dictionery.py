#key는 unique해야 하며, 불변 이다 , value 는 가변(변경 가능)
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])


dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
print ("dict['Alice']: ", dict['Alice'])  #존재하지 않는 키로 요소에 접근할 경우?

dict['Age'] = 8;  #요소의 value변경
dict['School'] = "DPS School"    #새로운 요소를 추가 
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict1['Name']  #특정 요소만 삭제
dict.clear()      #모든 요소를 삭제하고, dict 객체는 남고, empty dict instance가 된다.
del dict # dict  객체 삭제?
print(dict) #error?

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'} #오버라이팅된다. 엎어쓰기 된다.
print ("dict['Name']: ", dict['Name'])

dict = {['Name']: 'Zara', 'Age': 7} #키에 가변개체 선언(사용), 에러발생, 불변만 써야한다.
print ("dict['Name']: ", dict['Name'])


dict = {'Name': 'Zara', 'Age': 7}
print ("Value : %s" %  dict.items())
print ("Value : %s" %  dict.keys())
 
print ("Value : %s" %  dict.get('Age')) #없는 값을 요청할때
print ("Value : %s" %  dict.get('Sex', "NA"))

dict = {'Sex': 'female', 'Age': 7, 'Name': 'Zara'}
print ("Values : ",  list(dict.values()))

dict = {'Name': 'Manni', 'Age': 7, 'Class': 'First'} #dictionery 요소개수
print ("Length : %d" % len (dict))

#######################################################
dict1 = {'Name': 'Zara', 'Age': 7};
dict2 = {'Name': 'Mahnaz', 'Age': 27};
dict3 = {'Name': 'Abid', 'Age': 27};
dict4 = {'Name': 'Zara', 'Age': 7};
print "Return Value : %d" %  cmp (dict1, dict2)
print "Return Value : %d" %  cmp (dict2, dict3)
print "Return Value : %d" %  cmp (dict1, dict4)
