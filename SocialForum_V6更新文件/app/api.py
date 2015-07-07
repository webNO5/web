# -*- coding: utf-8 -*-
from flask import jsonify
from app import app

test={
    'name':'test',
    'id':121
}

@app.route('/api/v1.0/account/test', methods=['GET'])
def get_test():
    return jsonify({'test': test})
