# -*- coding: utf-8 -*-

from run import application


@application.route('/nefunguje')
def not_working():
    return jsonify({'api': 'fail'})


def omg():
    print('hello')


