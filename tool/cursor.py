from tool.settings import config
import pymysql
"""
tool工具 cursor封装了数据库连接池的方法

"""


def get_mysql_cursor():
    """
    get_mysql_cursor方法获取 tool 中的settings创建数据库连接池中获取一条连接
    并且获取 该连接的游标 返回 conn,cursor
    :return:
    """
    conn = config.POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
    return conn, cursor


def sql_end(conn, cursor):
    """
    用于封装连接数据库中结束后关闭游标以及将连接返回连接池的操作
    :param conn:
    :param cursor:
    :return:
    """
    cursor.close()
    conn.close()


def sql_fetchone(sql, args=None):
    """
    适用于sql查询后需要fetchone的操作
    :param sql:
    :param args:
    :return:
    """
    conn, cursor = get_mysql_cursor()
    cursor.execute(sql, args)
    ret = cursor.fetchone()
    sql_end(conn, cursor)
    return ret


def sql_fetchall(sql, args=None):
    """
    适用于sql查询后需要fetchall的操作
    :param sql:
    :param args:
    :return:
    """
    conn, cursor = get_mysql_cursor()
    cursor.execute(sql, args)
    ret = cursor.fetchall()
    sql_end(conn, cursor)
    return ret


def sql_commit(sql, args=None):
    """
    适用于sql插入提交操作
    :param sql:
    :param args:
    :return:
    """
    conn, cursor = get_mysql_cursor()
    ret = cursor.execute(sql, args)
    conn.commit()
    sql_end(conn, cursor)
    return ret
