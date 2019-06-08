import random

Month = random.randint(1, 12)
Day = random.randint(1, 30)
year = (2018, 2019)
YearChoice = random.choice(year)
if YearChoice==2019 and Month>6:
    NewMonth=random.randint(1,5)
    Month=NewMonth
print(YearChoice,Month,Day)