from flask import Flask, request, session, redirect
from .views import login
from .views import user_list


def get_app():
    app = Flask(__name__)
    app.config.from_object("tool.settings.config")

    app.register_blueprint(login.login_blueprint)
    app.register_blueprint(user_list.user_list_blueprint)

    @app.template_global()
    def get_user_name(uid):
        from tool.cursor import get_mysql_cursor
        conn, cursor = get_mysql_cursor()
        sql = "select username from user where id = %s"
        cursor.execute(sql, uid)
        ret = cursor.fetchone()
        return ret

    return app

