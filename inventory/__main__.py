"""
HSBXL inventory web app.
"""

import os.path
import json
from bottle import Bottle, template, static_file, response

bottle = Bottle()

HERE = os.path.dirname(os.path.realpath(__file__))


@bottle.route('/')
def index():
    return template(os.path.join(HERE, 'views/index'))


@bottle.route('/item/<name>')
def index(name):
    response.content_type = 'application/json'
    return json.dumps({"hello": "stuff"})


@bottle.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=os.path.join(HERE, 'static'))


bottle.run(debug=True, reloader=True, host='localhost', port=8080)
