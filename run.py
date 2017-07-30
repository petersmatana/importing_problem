# -*- coding: utf-8 -*-

from flask import Flask, jsonify
from flask_restful import Api

# from dir1.dir2.jee_here import DalsiPokus

application = Flask(__name__)
api = Api(application)

'''
@application.route('/funguje')
def working():
    return jsonify({'api': 'ok'})
'''

if __name__ == '__main__':
    application.run(port=5000, debug=True)
