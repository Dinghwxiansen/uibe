# -*- coding: utf-8 -*-
# @Time    :2019/11/23 14:06
# todo Python 数据库连接类，sql语句拼接方法

import MySQLdb
# todo 1 sql拼接方法
import dbpool as DBpool
from dateutil.relativedelta import relativedelta


def safe(s):
    return MySQLdb.escape_string(s)


def get_i_sql(table, dict):
    """ 生成insert的sql语句 @table，插入记录的表名 @dict,插入的数据，字典 """
    sql = 'insert into %s set ' % table
    sql += dict_2_str(dict)
    return sql


def get_s_sql(table, keys, conditions, isdistinct=0):
    """
        生成select的sql语句
    @table，查询记录的表名
    @key，需要查询的字段
    @conditions,插入的数据，字典
    @isdistinct,查询的数据是否不重复
    """
    if isdistinct:
        sql = 'select distinct %s ' % ",".join(keys)
    else:
        sql = 'select  %s ' % ",".join(keys)
    sql += ' from %s ' % table
    if conditions:
        sql += ' where %s ' % dict_2_str_and(conditions)
    return sql


def get_u_sql(table, value, conditions):
    """
        生成update的sql语句
    @table，查询记录的表名
    @value，dict,需要更新的字段
    @conditions,插入的数据，字典
    """
    sql = 'update %s set ' % table
    sql += dict_2_str(value)
    if conditions:
        sql += ' where %s ' % dict_2_str_and(conditions)
    return sql


def get_d_sql(table, conditions):
    """
        生成detele的sql语句
    @table，查询记录的表名

    @conditions,插入的数据，字典
    """
    sql = 'delete from  %s  ' % table
    if conditions:
        sql += ' where %s ' % dict_2_str_and(conditions)
    return sql


def dict_2_str(dictin):
    """
    将字典变成，key='value',key='value' 的形式
    """
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), safe(str(v)))
        tmplist.append(' ' + tmp + ' ')
    return ','.join(tmplist)


def dict_2_str_and(dictin):
    """
    将字典变成，key='value' and key='value'的形式
    """
    tmplist = []
    for k, v in dictin.items():
        tmp = "%s='%s'" % (str(k), safe(str(v)))
        tmplist.append(' ' + tmp + ' ')
    return ' and '.join(tmplist)


# todo 数据库连接类

class SqlConn():
    def __init__(self):
        self.conn = DBpool.pool.connection()
        self.cur = self.conn.cursor()

    def cur(self):
        return self.cur()

    def commit(self):
        self.conn.commit()

    def execute(self, sql, fetchone=0):
        self.cur.execute(sql)
        return self.cur.fetchone() if fetchone else self.cur.fetchall()

    def last_id(self, table):
        sql = 'SELECT LAST_INSERT_ID() from %s' % table
        return self.execute(sql, 1)[0]

    def close(self):
        self.cur.close()
        self.conn.close()


# 查询结果解析方法
def fSqlResult(r, key_list):
    # r @tuple 数据库fetchall的结果
    # key_list @list 查询字段的keys
    # format SQL Result 格式化数据库查询的结果，转化成包含多个字典的列表格式，即((1,2),(3,4))->[{"key1":1,"key2":2},{"key1":3,"key2":4}]
    # 返回 @dict 查询结果
    mlist = []
    l = len(key_list)
    if r:
        for item in r:
            tmp = {}
            for i in range(l):
                tmp[key_list[i]] = str(item[i])
            mlist.append(tmp)
    return mlist


list = ['SELECT zgh FROM jzg  WHERE xb=1', 'SELECT zgh FROM jzg WHERE zxxmsl >4 ', 'c']
# list = ['a', 'b ', 'c']
print(list[0]+' union all '+list[1]+' union all '+list[2])
bbb = len(list) - 1
aaa=' UNION ALL '.join(list)
print("bbb"+aaa +str(bbb))

# todo 结果
#     SELECT  zgh, COUNT(*)
#     FROM (SELECT zgh FROM jzg  WHERE xb=1 UNION ALL SELECT zgh FROM jzg WHERE zxxmsl >4 ) a
#     GROUP BY zgh
#     HAVING COUNT(*) > 1

# for i in list:
#     index = list.index(i)
#     print(index)

# for a in list:
#     index = list.index(a)
#     print(index)
#     list[index] +=" union all "
#
#     print(list[index])



import pytz
import datetime

tz = pytz.timezone('Asia/Shanghai')

user_time = datetime.datetime.now(tz).strftime("%Y-%m")

Last_month = datetime.date.today() - relativedelta(months=1)
print(Last_month)
print(user_time)


def gen_dates(b_date, days):
    day = datetime.timedelta(days=1)
    for i in range(days):
        yield b_date + day*i


def get_date_list(start=None, end=None):
    """
    获取日期列表
    :param start: 开始日期
    :param end: 结束日期
    :return:
    """
    if start is None:
        start = datetime.datetime.strptime("2000-01-01", "%Y-%m-%d")
    if end is None:
        end = datetime.datetime.now()
    data = []
    for d in gen_dates(start, (end-start).days):
        data.append(d)
    return data

if __name__ == "__main__":
    print(get_date_list())


from datetime import *

from dateutil.relativedelta import relativedelta

if __name__ == "__main__":
    print(datetime.today() - relativedelta(months=+1))
