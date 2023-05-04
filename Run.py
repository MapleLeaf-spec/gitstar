import datetime
import os
import random
def GetScourse():
    choices = (1, 2, 3)
    filesNumber = random.choice(choices)
    fileadd = str(filesNumber) + ".txt"
    with open(fileadd, 'a+') as Add:
        Add.write("1")
def commit():
    os.system('git commit -a -m test_github_streak > /dev/null 2>&1')

def set_sys_time():
    Month = random.randint(1, 12)
    Day = random.randint(1, 30)
    year = (2018, 2023)
    YearChoice = random.choice(year)
    if YearChoice == 2023 and Month > 5:
        NewMonth = random.randint(1, 4)
        Month = NewMonth
    cmd = f'date {YearChoice}-{Month:02d}-{Day:02d}'
    print(cmd)
    os.system(cmd)

def trick_commit():
    set_sys_time()
    print("设置时间执行完成")
    GetScourse()
    print("获取资源执行完成")
    commit()
    print("提交执行完成")
def gitPush():
    for x in range(1):
        trick_commit()
if __name__ == '__main__':
    gitPush()


