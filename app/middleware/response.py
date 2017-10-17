# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""

from http import HTTPStatus
from flask import make_response, jsonify, send_from_directory


def view(directory, filename):
    """
    Render view
    :param directory: str
    :param filename: str
    :return: str
    """

    return send_from_directory(directory, filename)


def created(message):
    """
    HTTP 201 / Created
    :param message: dict
    :return: str
    """

    return make_response(jsonify({
        'status': HTTPStatus.CREATED,
        'message': message
    }), HTTPStatus.CREATED)


def not_found(data):
    """
    HTTP 404 / Not found
    :param data: str
    :return: str
    """

    message = str(data)

    return make_response(jsonify({
        'status': HTTPStatus.NOT_FOUND,
        'message': message
    }), HTTPStatus.NOT_FOUND)


def bad_request(data):
    """
    HTTP 400 / Bad request
    :param data: str
    :return: str
    """

    message = str(data)

    return make_response(jsonify({
        'status': HTTPStatus.BAD_REQUEST,
        'message': message
    }), HTTPStatus.BAD_REQUEST)
