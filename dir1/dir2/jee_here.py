# -*- coding: utf-8 -*-

from flask_restful import Resource
from run import api

'''
@application.route('/nefunguje')
def not_working():
    return jsonify({'api': 'fail'})
'''


class DalsiPokus(Resource):

    def get(self):
        return {'api': 'ok'}

api.add_resource(DalsiPokus, '/dalsi_pokus')

