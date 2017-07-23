import flask
import json
from . json_encoder import JSONEncoder
from flask import Flask
from flask import request
from flask.ext.cors import CORS

from cellcraft_node.mongo import insert_items_mongo, get_items_mongo, get_item_by_id


app = Flask(__name__, static_url_path='/static')
CORS(app)


# @app.route('/css/<path:path>')
# def serve_css(path):
#     return send_from_directory('css', path)


# @app.route('/img/<path:path>')
# def serve_images(path):
#     return send_from_directory('img', path)


# @app.route('/js/<path:path>')
# def serve_js(path):
#     return send_from_directory('js', path)


@app.route('/items/<_id>', methods=['GET'])
def get_single_item(_id):
    try:
        response = {'data': get_item_by_id(_id)}
        print(response)
        code = 200
    except:
        response = {}
        code = 500
    return json.dumps(response, cls=JSONEncoder), code


@app.route('/items', methods=['GET'])
def get_items():
    try:
        args = request.args.to_dict()
        print(args)
        response = {'data': get_items_mongo(query=args)}
        print(response)
        code = 200
    except:
        response = {}
        code = 500
    return json.dumps(response, cls=JSONEncoder), code


@app.route('/items', methods=['POST'])
def post_items():
    r = request.get_json()
    print('Object to insert', r)
    try:
        response = {'data': insert_items_mongo(r['data'])}
        code = 200
    except:
        response = {}
        code = 500
    return flask.jsonify(response), code


def start():
    app.run('0.0.0.0',
            port=4534,
            debug=True,
            use_debugger=False,
            use_reloader=True)
