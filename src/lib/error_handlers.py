""" Error handlers"""
import flask
from flask import jsonify

blueprint = flask.Blueprint("error_handlers", __name__)


@blueprint.app_errorhandler(400)
def not_found(error):
    """error:400"""
    return (
        jsonify({"code": error.code, "name": error.name, "description": error.description}),
        400,
    )


@blueprint.app_errorhandler(404)
def bad_request(error):
    """error:404"""
    return (
        jsonify({"code": error.code, "name": error.name, "description": error.description}),
        404,
    )


@blueprint.app_errorhandler(405)
def method_not_allowed(error):
    """error:405"""
    return (
        jsonify({"code": error.code, "name": error.name, "description": error.description}),
        405,
    )


@blueprint.app_errorhandler(413)
def request_entity_too_large(error):
    """error:413"""
    return (
        jsonify({"code": error.code, "name": error.name, "description": error.description}),
        413,
    )


@blueprint.app_errorhandler(414)
def request_uri_too_long(error):
    """error:414"""
    return (
        jsonify({"code": error.code, "name": error.name, "description": error.description}),
        414,
    )


@blueprint.app_errorhandler(500)
def internal_server_error(error):
    """error:500"""
    return (
        jsonify({"code": error.code, "name": error.name, "description": error.description}),
        500,
    )
