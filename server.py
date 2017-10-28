import uuid
import os, errno
import imghdr
from animations import bunnies, mirror

import flask
from flask import Flask
from flask import request

app = Flask(__name__, static_folder='FSPT', static_url_path='')

@app.route("/jobs")
def jobs():
    return flask.render_template('jobs.html', foo=42)

@app.route("/")
def root():
    return app.send_static_file('index.html')

@app.route("/scene/<path:filename>")
def animation(filename):
    return mirror.get_frame_config(int(request.args.get('frame')))

@app.route("/<path:filename>")
def asset(filename):
    return app.send_static_file(filename)

@app.route("/upload/<scene_name>/<frame_number>", methods=["POST"])
def upload(scene_name, frame_number):
    try:
        os.makedirs('outputs')
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

    path_name = 'outputs/{}_{}.png'.format(scene_name, frame_number)
    if imghdr.what('', h=request.data) == 'png':
        with open(path_name, 'wb') as fd:
            fd.write(request.data)
            fd.close()
        return "", 201
    else:
        return "", 400


#app.run(port=8080)