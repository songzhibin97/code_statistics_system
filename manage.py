from code_statistics_system import get_app
from flask import request, session, redirect
import re

app = get_app()

if __name__ == "__main__":
    @app.before_request
    def get_user():
        if request.path == '/login' or re.search('/static', request.path):
            return None
        user = session.get("user")
        if user:
            return None
        return redirect('/login')


    app.run()
