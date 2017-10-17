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
    import configparser
    from logging.handlers import RotatingFileHandler
    from flask import Flask, request
    from modules import ImageUploader, ImageUploaderError
    from middleware import response

    config = configparser.ConfigParser()
    config.read('config.ini')
    handler = RotatingFileHandler(config['logger']['filename'],
                                  maxBytes=int(config['logger']['maxbytes']),
                                  backupCount=int(config['logger']['backup_count']))
    handler.setLevel(logging.INFO)

    try:
        application = Flask(__name__)
        application.config['MAX_CONTENT_LENGTH'] = int(config['upload']['maxbytes'])

        @application.route('/')
        def index():
            """
            API Doc route
            :return: str
            """

            return response.view(config['static']['directory'], 'index.html')


        """
        @api {post} /upload/:uid Upload user profile photo
        @apiName Upload Profile Photo
        @apiGroup FaceDetect API
        @apiDescription Upload user profile photo
        @apiPermission authenticated user
        
        @apiParam {String} file User file mutipart/form-data
        
        @apiSuccess {Number} status HTTP 201 Created
        @apiSuccess {Object[]} message  Success upload message
        
        @apiSuccessExample Success-Response
            HTTP/1.1 201 Created
            {
                "status": 201,
                "message": {
                    "uid": 1507343002,
                    "original": "http://localhost/images/1507343002/original.jpg",
                    "thumbnail": "http://localhost/images/1507343002/thumbnail.jpg",
                    "minify": "http://localhost/images/1507343002/minify.jpg"
                }
            }
        
        @apiError ImageUploaderError Request does not match real req data
        
        @apiErrorExample ImageUploaderError
            HTTP/1.1 400 Bad Request
            {
                "status": 400,
                "message": "Invalid request data"
            }
        """
        @application.route('/upload/<int:uid>', methods=['POST'])
        def upload(uid):
            """
            Upload and handle user image
            :return: str
            """

            try:
                data = ImageUploader().process(uid, request.files)
                return response.created(data)
            except ImageUploaderError as e:
                return response.bad_request(e)


        @application.errorhandler(404)
        def not_found(error):
            """
            Page not found
            :param error: str
            :return:
            """

            return response.not_found(error)

        application.run(
            host=config['server']['host'],
            port=int(config['server']['port']),
            debug=config['server']['debug']
        )

    except Exception as error:
        sys.exit(error)
