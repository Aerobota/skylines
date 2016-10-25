from flask import Blueprint, request, jsonify

from skylines import api
from skylines.api.views.parser import parse_location

mapitems_blueprint = Blueprint('mapitems', 'skylines')


@mapitems_blueprint.route('/mapitems', strict_slashes=False)
def list():
    location = parse_location(request.args)
    return jsonify({
        'airspaces': api.get_airspaces_by_location(location),
        'waves': api.get_waves_by_location(location),
    })
