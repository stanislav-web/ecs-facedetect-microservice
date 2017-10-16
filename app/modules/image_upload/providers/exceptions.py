# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""


class UploadProviderError(Exception):
    """UploadProviderError class"""

    def __init__(self, message):
        """
        Error message
        :param message: message
        :return: None
        """

        super(UploadProviderError, self).__init__(message)


class ResizeProviderError(Exception):
    """ResizeProviderError class"""

    def __init__(self, message):
        """
        Error message
        :param message: message
        :return: None
        """

        super(ResizeProviderError, self).__init__(message)
