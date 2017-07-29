# -*- coding: utf-8 -*-

from flask import Flask, jsonify


application = Flask(__name__)


@application.route('/funguje')
def working():
    return jsonify({'api': 'ok'})

if __name__ == '__main__':
    application.run(port=5000, debug=True)
