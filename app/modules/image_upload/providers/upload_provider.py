# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""

import os
from .lib import FileSystem
from .exceptions import UploadProviderError


class UploadProvider(object):
    """ UploadProvider class"""

    def __init__(self):
        """
        Init UploadProvider class
        """

        config = FileSystem.readcfg('config.ini')
        self.config = config['upload']

    def _get_allowed_extensions(self):
        """
        Get allowed for uploading extensions

        :return: list
        """

        extensions_list = self.config['extensions'].split(',')
        return extensions_list

    def _is_allowed_extension(self, filename):
        """
        Check file extension

        :param str filename:
        :return:
        """

        return '.' in filename and \
               filename.rsplit('.', 1)[1].lower() in self._get_allowed_extensions()

    def _is_allowed_size(self, file):
        """
        Check file size

        :param FileStorage file:
        :return: bool
        """

        file_length = len(file.stream.getvalue())
        return 0 < file_length <= int(self.config['maxbytes'])

    def format_url(self, uid, imagepath):
        """
        Format asb path to server uri

        :param uid: int user id
        :param imagepath: image abspath
        :return: str
        """

        return self.config['urlpath'].format(uid=uid, image=os.path.basename(imagepath))

    def upload(self, uid, request):
        """
        Upload file by params
        :param uid str user identifier
        :param request ImmutableMultiDict
        :raise UploadProviderError
        :return: str
        """

        try:
            if 'file' not in request:
                raise UploadProviderError('No file specified')

            file = request['file']

            if not file or not bool(file.filename):
                raise UploadProviderError('No filename specified')

            if not self._is_allowed_extension(file.filename):
                raise UploadProviderError('Invalid file extension. Allowed {0}'.format(self.config['extensions']))

            if not self._is_allowed_size(file):
                raise UploadProviderError('File entity too large')

            dirname = self.config['save_path'].format(uid=uid)
            extension = os.path.splitext(file.filename)[1]
            filename = "{0}{1}".format(self.config['original'], extension)

            FileSystem.makedir(dirname)
            file.save(os.path.join(dirname, filename))
            return os.path.realpath(os.path.join(os.path.join(dirname, filename)))
        except Exception as error:
            raise UploadProviderError(error)

    def remove(self, uid):
        """
        Remove directory
        :param uid: int user id
        :return: None
        """
        dirname = self.config['save_path'].format(uid=uid)
        FileSystem.remove(dirname)
        pass
