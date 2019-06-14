# 1. 加密
# import hashlib
# hash = hashlib.md5(b"sdf1123df")
#
# hash.update(bytes('123',encoding='utf-8'))
#
# ret = hash.hexdigest()
# print(ret)


# 2. 数据库操作
# import pymysql
#
# conn = pymysql.Connect(host='127.0.0.1',user='root',password='123456',database='s9day118',charset='utf8')
#
# cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#
# # 不要这么用
# # sql = "select * from userinfo where user='%s' and pwd ='%s'" %("xiao ' or 1=1 -- ","47f5abdd7f4083f0cc5c94d587fa3ca4")
#
# # cursor.execute("select * from userinfo where user=%s and pwd =%s",("xiaoqiang","47f5abdd7f4083f0cc5c94d587fa3ca4"))
# cursor.execute("select * from userinfo where user=%(us)s and pwd =%(pw)s",{"us":"xiaoqiang","pw":"47f5abdd7f4083f0cc5c94d587fa3ca4"})
#
# # data = cursor.fetchall()
# data = cursor.fetchone()
#
# cursor.close()
# conn.close()
#
# print(data)

# 3. 解压文件


import shutil

shutil._unpack_zipfile(r"E:\wupeiqi\s9\homework-晓强\homework\files\luffy-vue简单示例（一）.zip",r"E:\wupeiqi\s9\homework-晓强\homework\xxx")



