# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""

import errno
import os
import shutil
from configparser import RawConfigParser, ParsingError, NoOptionError
from .exceptions import FileSystemError


class FileSystem(object):
    """FileSystem class"""

    sep = os.sep

    @staticmethod
    def is_exist(directory, filename):
        """
        Check if dir-file is exist
        :param str directory: directory
        :param str filename: filename
        :return: bool
        """

        path = os.path.join(directory, filename)
        if not os.path.exists(path):
            return False
        else:
            return True

    @staticmethod
    def makedir(directory, mode=0o777):
        """
        Create new directory

        :param str directory: directory
        :param int mode: directory permission
        :raise: FileSystemError
        :return: str
        """

        if not os.path.exists(directory) or not os.access(directory, os.W_OK):

            try:
                directory = os.path.join(directory)
                directory += '/'
                os.makedirs(directory, mode=mode)
            except OSError:
                try:
                    directory = os.path.join(os.path.expanduser('~'), directory)
                    os.makedirs(directory, mode=mode)
                except OSError as error:
                    if error.errno != errno.EEXIST:
                        raise FileSystemError("Cannot create directory `{0}`. Reason: {1}".format(directory, error))
        return directory

    @staticmethod
    def getabsname(filename):
        """
        Get absolute file path
        :param str filename: directory
        :return: str
        """

        filename = os.path.join(filename)
        return os.path.abspath(filename)

    @staticmethod
    def get_extension(line):
        """
        Get extension from line
        :param str line: input string
        :return: str
        """

        ext = os.path.splitext(line)[-1]
        return ext

    @staticmethod
    def readcfg(filename):
        """
        Read .cfg file
        :param str filename: input filename
        :raise FileSystemError
        :return: configparser.RawConfigParser
        """

        if not os.path.isfile(filename):
            raise FileSystemError("{0} is not a file ".format(filename))
        if not os.access(filename, os.R_OK):
            raise FileSystemError("Configuration file {0} can not be read. Setup chmod 0644".format(filename))

        try:

            config = RawConfigParser()
            config.read(filename)
            return config

        except (ParsingError, NoOptionError) as error:
            raise FileSystemError(error)

    @staticmethod
    def remove(directory):
        """
        Remove directory
        :param str directory: os directory
        :raise: FileSystemError
        :return: None
        """

        if True is os.path.exists(directory):
            try:
                shutil.rmtree(os.path.join(directory))
            except IOError as error:
                raise FileSystemError(error.strerror)
