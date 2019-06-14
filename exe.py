import pymysql
import re
import os
import datetime
from tool.cursor import get_mysql_cursor

if __name__ == "__main__":
    conn = pymysql.connect(host='203.195.171.208', port=3306, database='flask_demo',
                           user='bin', password='123')
    # cursor = conn.cursor()
    # username = 'songzhibin'
    # password = '123'
    # # sql = 'show tables'
    # # sql = "alter table details modify column username int(128)"
    # # sql = "alter table details add constraint fk_details_user foreign key details(username) references user(id)"
    # # sql = "create table details(id int auto_increment primary key ,username varchar(128),time DATETIME,row int(255))ENGINE=InnoDB DEFAULT CHARSET=utf8"
    # cursor.execute("select id from details where username=%s and time=%s",(1,datetime.date.today()))
    # ret = cursor.fetchall()
    # print(ret)
    # path = "/Users/songzhibin/pycharm_program/code_statistics_system/code_statistics_system/views/statics/push/BBS项目.txt"
    # with open(path, 'rb') as f:
    #     print(f.read().decode('gbk'))
    # now_time = datetime.datetime.now()
    # sql = "INSERT INTO details(username,row,time) VALUES (%s,%s,%s)"
    # cursor = get_mysql_cursor()
    # cursor.execute(sql, [1, 200, now_time])
    # print(cursor.fetchall())
    list = [{'username': 1, 'row': 3263, 'time': datetime.date(2019, 4, 23)},
            {'username': 1, 'row': 10, 'time': datetime.date(2019, 4, 22)},
            {'username': 1, 'row': 15, 'time': datetime.date(2019, 4, 21)}]
    print(list.reverse())
    print(list)
    """
    var options = {
  "xAxis": [
    {
      "type": "category",
      "categories": [
        "非洲",
        "美洲",
        "亚洲",
        "欧洲",
        "大洋洲"
      ],
      "title": {
        "text": ""
      },
      "index": 0,
      "isX": true
    }
  ],
  "series": [
    {
      "name": "1800年",
      "data": [
        107,
        31,
        635,
        203,
        2
      ],
      "_colorIndex": 0
    },
    {
      "name": "1900年",
      "data": [
        133,
        156,
        947,
        408,
        6
      ],
      "_colorIndex": 1
    },
    {
      "name": "2008年",
      "data": [
        973,
        914,
        4054,
        732,
        34
      ],
      "_colorIndex": 2
    }
  ],
  "yAxis": [
    {
      "title": {
        "text": "人口总量 (百万)",
        "align": "high"
      },
      "labels": {
        "align": "center"
      },
      "index": 0
    }
  ],
  "chart": {
    "style": {
      "fontFamily": "\"微软雅黑\", Arial, Helvetica, sans-serif",
      "color": "#333",
      "fontSize": "12px",
      "fontWeight": "normal",
      "fontStyle": "normal"
    },
    "type": "column",
    "inverted": true
  },
  "title": {
    "text": "各洲不同时间的人口条形图"
  },
  "subtitle": {
    "text": "数据来源: Wikipedia.org"
  },
  "tooltip": {
    "valueSuffix": " 百万"
  },
  "legend": {
    "layout": "vertical",
    "align": "right",
    "verticalAlign": "top",
    "x": -40,
    "y": 100,
    "floating": true,
    "borderWidth": 1
  },
  "plotOptions": {
    "series": {
      "dataLabels": {
        "enabled": true,
        "allowOverlap": true
      },
      "animation": false
    }
  }
}
    """
    pass
