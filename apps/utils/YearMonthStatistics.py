# -*- coding: utf-8 -*-
# @Time    :2020/1/17 15:19
import calendar
import datetime
import time

"""获取所有月返回列表"""


def getBetweenMonth(begin_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m")
        date_list.append(date_str)
        begin_date = add_months(begin_date, 1)
    return date_list


def add_months(dt, months):
    month = dt.month - 1 + months
    year = dt.year + month // 12
    month = month % 12 + 1
    day = min(dt.day, calendar.monthrange(year, month)[1])
    return dt.replace(year=year, month=month, day=day)


"""获取所有季度，返回列表"""


# def getBetweenMonth(begin_date):
#     date_list = []
#     begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
#     end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")
#     while begin_date <= end_date:
#         date_str = begin_date.strftime("%Y-%m")
#         date_list.append(date_str)
#         begin_date = add_months(begin_date, 1)
#     return date_list
#
#
# def add_months(dt, months):
#     month = dt.month - 1 + months
#     year = dt.year + month / 12
#     month = month % 12 + 1
#     day = min(dt.day, calendar.monthrange(year, month)[1])
#     return dt.replace(year=year, month=month, day=day)


def getBetweenQuarter(begin_date):
    quarter_list = []
    month_list = getBetweenMonth(begin_date)
    for value in month_list:
        tempvalue = value.split("-")
        if tempvalue[1] in ['01', '02', '03']:
            quarter_list.append(tempvalue[0] + "Q1")
        elif tempvalue[1] in ['04', '05', '06']:
            quarter_list.append(tempvalue[0] + "Q2")
        elif tempvalue[1] in ['07', '08', '09']:
            quarter_list.append(tempvalue[0] + "Q3")
        elif tempvalue[1] in ['10', '11', '12']:
            quarter_list.append(tempvalue[0] + "Q4")
    quarter_set = set(quarter_list)
    quarter_list = list(quarter_set)
    quarter_list.sort()
    return quarter_list


"""获取所有天 返回列表"""


def getBetweenDay(begin_date):
    date_list = []
    begin_date = datetime.datetime.strptime(begin_date, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(time.strftime('%Y-%m-%d', time.localtime(time.time())), "%Y-%m-%d")
    while begin_date <= end_date:
        date_str = begin_date.strftime("%Y-%m-%d")
        date_list.append(date_str)
        begin_date += datetime.timedelta(days=1)
    return date_list


if __name__ == "__main__":
    # print(get_date_list())
    import datetime

    today = datetime.date.today()
    from dateutil.relativedelta import relativedelta  # 需要引入新的包

    last_2_month = today + relativedelta(months=-12)  # 上两个月，上N个月参数为(months=-N)
    dateddd = datetime.datetime.strftime(last_2_month, "%Y-%m-%d")
    print(getBetweenMonth(dateddd))
