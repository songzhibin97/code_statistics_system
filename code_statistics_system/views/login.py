from flask import Blueprint, request, render_template, session, redirect
from tool.cursor import sql_fetchone

login_blueprint = Blueprint("login_blueprint", __name__)


@login_blueprint.route('/login', methods=['get', 'post'])
def login():
    """
    处理用户登录
    :return:
    """
    if request.method == 'GET':
        return render_template('login.html')
    username = request.form.get("username")
    password = request.form.get("password")
    sql = "select id from user where username=%s and password=%s"
    uid = sql_fetchone(sql, (username, password))
    if uid:
        session['user'] = {"user": uid.get('id')}
        return '登录成功'
    return render_template('login.html', error='账户或密码错误')


@login_blueprint.route('/logout')
def logout():
    """
    处理用户注销
    :return:
    """
    session.pop("user", None)
    return redirect('/login')

