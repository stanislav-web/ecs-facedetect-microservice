# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""

import sys

if __name__ == "__main__":

    import logging
    from logging.handlers import RotatingFileHandler
    from flask import Flask, request, jsonify
    import configparser
    from lib import ImageUpload

    config = configparser.ConfigParser()
    config.read('config.ini')
    handler = RotatingFileHandler(config['logger']['filename'],
                                  maxBytes=int(config['logger']['maxbytes']),
                                  backupCount=int(config['logger']['backup_count']))
    handler.setLevel(logging.INFO)

    try:
        application = Flask(__name__)


        @application.route('/')
        def index():
            """
            API Doc route
            :return: None
            """

            return None


        @application.route('/upload', methods=['POST'])
        def upload():
            """
            Upload and handle user image
            :return: str
            """

            try:
                data = ImageUpload().process(request.files)
                return jsonify(data)
            except Exception as err:
                return jsonify({'status': 500, 'message': err})


        application.run(
            host=config['server']['host'],
            port=int(config['server']['port']),
            debug=config['server']['debug']
        )

    except Exception as error:
        sys.exit(error)
