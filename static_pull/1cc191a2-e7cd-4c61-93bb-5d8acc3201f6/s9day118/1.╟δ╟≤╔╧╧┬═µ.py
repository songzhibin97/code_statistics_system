# by luffycity.com
import redis
from flask import Flask,request,session
from rest_framework.serializers import Serializer
from flask import globals



app = Flask(__name__)


@app.route('/home')
def index():

    return '...'


if __name__ == '__main__':
    app.run()
    app.__call__
    app.wsgi_app