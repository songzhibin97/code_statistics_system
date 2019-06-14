from flask import Blueprint, session, render_template, request
from tool.cursor import sql_fetchall, sql_commit, sql_fetchone
import os
import datetime
import shutil
import uuid
import json
user_list_blueprint = Blueprint("user_list_blueprint", __name__)


@user_list_blueprint.route('/user_list')
def user_list():
    """
    处理展示用户列表
    :return:
    """
    uid = session.get('user').get('user')
    sql = "select username,row,time from details order by time desc "
    data = sql_fetchall(sql)
    data.reverse()
    return render_template('user_list.html', **{"data": data, 'uid': uid})


@user_list_blueprint.route('/show_list', methods=['GET', 'POST'])
def show_list():
    """
    get请求展示个人提交记录
    post请求展示图表结构
    :return:
    """
    uid = session.get('user').get('user')
    sql = "select username,row,time from details where username=%s order by time desc limit 31"
    data = sql_fetchall(sql, uid)
    data.reverse()
    if request.method == 'GET':
        return render_template('show_list.html', **{"data": data, 'uid': uid})
    # 获取当前用户提交过的所有数据进行返回填充图表
    # 后端构建图表列表
    chart_list = []
    # 创建折线图字典
    chart_dict = {}
    # 起始时间轴
    start_point = []
    # 折线图数据 data 在循环中做
    line_data = []
    # 柱状图数据
    histogram_data = []
    # 循环前设置标记量
    histogram_sum = 0
    for da in data:
        da['time'] = str(da["time"])
        start_point.append(da['time'])
        line_data.append(da['row'])
        histogram_sum += int(da['row'])
        histogram_data.append(histogram_sum)
    # 构建字典结构
    chart_dict["start_point"] = start_point
    chart_dict["line_data"] = line_data
    chart_dict["histogram_data"] = histogram_data
    chart_list.append(chart_dict)
    json_data = json.dumps(chart_list)
    return json_data


@user_list_blueprint.route('/push_file', methods=["post"])
def push_file():
    """
    处理用户提交文件
    :return:
    """
    try:
        uid = session.get("user").get('user')  # 获得当前登录用户的uid 用于插入完成后数据库中提交数据
        files = request.files.get("files")
        now_time = datetime.date.today()
        # 进行判断 是否该用户今天已经提交过代码
        judgement_sql = "select id from details where username=%s and time=%s "
        ret = sql_fetchone(judgement_sql, (uid, now_time))
        if ret:
            return "您今天已经提交过代码啦"
        files_suffix = files.filename.rsplit(".", maxsplit=1)  # 从右向左 以"."进行切以分获得后缀名
        if len(files_suffix) != 2:  # 判断上传文件是否携带后缀
            return "上传格式有误,请上传压缩的zip包"
        if files_suffix[1] != 'zip':  # 判断上传文件是否是zip压缩文件
            print("no zip")
            return "上传格式有误,请上传压缩的zip包"
        # 处理上传的zip文件
        # 直接将zip文件解压至static_pull文件夹 文件地址
        decompression_path = os.path.join('static_pull', str(uuid.uuid4()))
        shutil._unpack_zipfile(files, decompression_path)  # 使用_unpack_zipfile 边读边压缩
        # 压缩完成后 循环读每一个文件读取相应的行数
        global_line = 0
        for root, dirs, file in os.walk(decompression_path):
            # 判断每一个文件的后缀
            for file_name in file:
                file_path = os.path.join(root, file_name)  # 当前遍历到的文件路径 用于打开文件使用
                file_suffix = file_name.rsplit(".", maxsplit=1)
                if len(file_suffix) != 2:  # 如果没有后缀 则不处理
                    continue
                if file_suffix[1] != 'py':  # 如果不是py文件 则不处理
                    continue
                line = 0  # 设置标记位 记录单个文件的行数
                with open(file_path, 'rb') as f:
                    for i in f:
                        i = i.strip()
                        if not i:  # 如果是空行则不计算
                            continue
                        if i.startswith(b'#'):
                            continue
                        line += 1
                global_line += line
        sql = "insert into details(username,row,time) values (%s,%s,%s)"
        sql_commit(sql, (uid, global_line, now_time))
        return "上传成功"
    except Exception as e:
        print(e)
        return "上传失败"
