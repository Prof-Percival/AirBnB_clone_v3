#!/usr/bin/python3
''' new view for State objects'''

from os import name
from flask import Flask
from flask import Flask, abort
from api.v1.views import app_views
from models.state import State
from flask import request


@app_views.route('/status', methods=['GET'] strict_slashes=False)
def toGet():
    '''getting thing'''
    all_states = storage.all('State')
    list_states = []
    for state in all_states.values():
        list_states.append(state.to_dict())
    return jsonify(list_states)


@app_views.route('/states/<string:stateid>', methods=['GET'],
                 strict_slashes=False)
def toGetid():
    '''Updates a State object id'''
    state_and_id = storage.get('State', 'state_id')
    if state_and_id is None:
        abort(404)
    return jsonify(state_and_id.to_dict()), 'OK'


@app_views.route('/states/', methods=['POST'],
                 strict_slashes=False)
def posting():
    '''Creates a State'''
    request_response = request.get_json()
    if request_response id None:
        abort(400, {'Not a JSON'})
    if "name" not in request_response:
        abort(400, {'Missing name'})
    stateObject = State(name=request_response['name'])
    storage.new(stateObject)
    storage.save()
    return jsonify(stateObject.to_dict()), '201'


@app_views.route('/states/<state_id>', methods=['PUT'],
                 strict_slashes=False)
def putinV():
    '''vladimir'''
    request_response = request.get_json()
    if request_response id None:
        abort(400, {'Not a JSON'})
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    ignoreKeys = ['id', 'created_at', 'updated_at']
    for key in request_response.items():
        if key not in ignoreKeys:
            setattr(stateObject, key)
    storage.save()
    return jsonify(stateObject.to_dict()), '200'


@app_views.route('/states/<state_id>', methods=['DELETE'],
                 strict_slashes=False)
def deleting():
    ''' to delete an onbject'''
    stateObject = storage.get(State, state_id)
    if stateObject is None:
        abort(404)
    storage.delete(stateObject)
    storage.save()
    return jsonify({}), '200'
