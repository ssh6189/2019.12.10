import os
    
class monster:
    def status(at, df):
        ats = at
        dfs = df


mk = monster()

mk.at = int(input("몬스터의 공격력을 입력하시오."))
mk.df = int(input("몬스터의 방어력을 입력하시오."))

os.system('cls')

print(mk.at)
print(mk.df)
