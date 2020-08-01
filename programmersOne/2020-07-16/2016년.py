# *
import datetime


def solution(a, b):
    answer = ''
    week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
    dt = datetime.datetime(2016, 1, 1)
    dtdt = datetime.datetime(2016, a, b)

    if(dt.weekday() == 4):
        dtdtWeekday = dtdt.weekday()
        answer = week[dtdtWeekday]

    return answer
