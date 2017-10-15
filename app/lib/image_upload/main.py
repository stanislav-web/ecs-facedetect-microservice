# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""

import os
from werkzeug.utils import secure_filename
from .filesystem import FileSystem
from .exceptions import ImageUploadError


class ImageUpload(object):
    """ImageUpload class"""

    def __init__(self):
        """
        Init ImageUpload class
        """

        config = FileSystem.readcfg('config.ini')
        self.config = config['upload']

    def get_allowed_extensions(self):
        """
        Get allowed for uploading extensions

        :return: list
        """

        extensions_list = self.config['extensions'].split(',')
        return extensions_list

    def is_allowed_extension(self, filename):
        """
        Check file extension

        :param str filename:
        :return:
        """

        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self.get_allowed_extensions()

    def process(self, request):
        """
        Upload file by params
        :param request ImmutableMultiDict
        :raise ImageUploadError
        :return: bool
        """

        try:
            if 'file' not in request:
                raise ImageUploadError('No file specified')

            file = request['file']
            if not bool(file.filename):
                raise ImageUploadError('No filename specified')

            if self.is_allowed_extension(file.filename):
                filename = secure_filename(file.filename)
                FileSystem.makedir(self.config['path'])

                file.save(os.path.join(self.config['path'], filename))
        except Exception as error:
            raise ImageUploadError(error)
