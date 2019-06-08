import datetime
import os
import random
def GetScourse():
    choices = (1, 2, 3)
    filesNumber = random.choice(choices)
    fileadd = str(filesNumber) + ".txt"
    with open(fileadd, 'w+') as Add:
        Add.write("1")
def commit():
    os.system('git commit -a -m test_github_streak > /dev/null 2>&1')

def set_sys_time():
    Month = random.randint(1, 12)
    Day = random.randint(1, 30)
    year = (2018, 2019)
    YearChoice = random.choice(year)
    if YearChoice == 2019 and Month > 6:
        NewMonth = random.randint(1, 5)
        Month = NewMonth
    os.system('date -s %04d%02d%02d' % (YearChoice, Month, Day))

def trick_commit():
    set_sys_time()
    GetScourse()
    commit()


if __name__ == '__main__':
    for x in range(600):
        trick_commit()


