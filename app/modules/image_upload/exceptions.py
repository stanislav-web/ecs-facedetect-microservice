# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""


class ImageUploaderError(Exception):
    """ImageUploaderError class"""

    def __init__(self, message):
        """
        Error message
        :param message: message
        :return: None
        """

        super(ImageUploaderError, self).__init__(message)
