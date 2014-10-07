"""
HSBXL inventory web app.
"""

import os.path
import json

from bottle import Bottle, template, static_file, response
import rethinkdb as r

HERE = os.path.dirname(os.path.realpath(__file__))


bottle = Bottle()
r.connect("localhost", 28015).repl()

if "inventory" not in r.db_list().run():
    r.db_create("inventory").run()
    r.db("inventory").table_create("items").run()

items = r.db("inventory").table("items")


@bottle.route('/')
def index():
    return template(os.path.join(HERE, 'views/index'))


@bottle.route('/item/')
def index():
    all_items = items.run()
    return template(os.path.join(HERE, 'views/items'), items=all_items)


@bottle.route('/item.json')
def index():
    response.content_type = 'application/json'
    response.set_header('Access-Control-Allow-Origin', '*')
    return json.dumps(list(items.run()))


@bottle.route('/item/<name>')
def index(name):
    response.content_type = 'application/json'
    return json.dumps(items.get(name).run())


@bottle.route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root=os.path.join(HERE, 'static'))


bottle.run(debug=True, reloader=True, host='0.0.0.0', port=8000)
