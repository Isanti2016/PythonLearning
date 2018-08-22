# -*- coding:utf-8 -*-

from enum import Enum,unique
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

@unique
class Weekday(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6


if __name__=='__main__':
    from enum_test import Weekday,Month
    day1=Weekday.Mon
    print(day1)

    print(Weekday['Tue'])

    print(Weekday.Fri.value)

    for name,member in Month.__members__.items():
        print(name,'=>',member,',',member.value)
