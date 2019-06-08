import datetime
import os
import random
#随机资源提交
def GetScourse():
    choices = (1, 2, 3)
    filesNumber = random.choice(choices)
    fileadd = str(filesNumber) + ".txt"
    with open(fileadd, 'w+') as Add:
        Add.write("1")
# 提交修改
def commit():
    os.system('git commit -a -m test_github_streak > /dev/null 2>&1')

#设置系统时间位为随机时间 注意 时间不能高于当前时间 大于当前时间需要设置为合理的时间范围
def set_sys_time():
    Month = random.randint(1, 12)
    Day = random.randint(1, 30)
    year = (2018, 2019)
    YearChoice = random.choice(year)
    if YearChoice == 2019 and Month > 6:
        NewMonth = random.randint(1, 5)
        Month = NewMonth
    os.system('date -s %04d%02d%02d' % (YearChoice, Month, Day))

#设置时间 提交随机资源 提交
def trick_commit():
    set_sys_time()
    GetScourse()
    commit()


if __name__ == '__main__':
    for x in range(600):
        trick_commit()


