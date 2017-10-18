# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""

import os
import cv2
from .exceptions import FaceDetectorError


class FaceDetector(object):
    """FaceDetector class"""

    CASCADE_PATTERN = 'modules/face_detect/templates/haarcascade_frontalface_default.xml'

    # Parameter specifying how much the image size is reduced at each image scale.
    SCALE_FACTOR = 1.3
    # Parameter specifying how many neighbors each candidate rectangle should have to retain it
    MIN_NEIGHBORS = 5

    # Minimum possible object size. Objects smaller than that are ignored
    MIN_SIZE = (1, 1)

    # Maximum possible object size. Objects larger than that are ignored
    MAX_SIZE = (128, 128)

    def __init__(self):
        """
        Init FaceDetector class
        """
        cascade_pattern_path = os.path.abspath(self.CASCADE_PATTERN)

        # using Haar's cascade pattern
        self.faceCascade = cv2.CascadeClassifier(cascade_pattern_path)

    def process(self, imagesrc):
        """
        Process image
        :param imagesrc string image path
        :raise FaceDetectorError
        :return: bool
        """

        try:

            gray = cv2.imread(imagesrc, cv2.IMREAD_GRAYSCALE)
            faces = self.faceCascade.detectMultiScale(gray,
                                                      scaleFactor=self.SCALE_FACTOR,
                                                      minNeighbors=self.MIN_NEIGHBORS,
                                                      flags=0,
                                                      minSize=self.MIN_SIZE,
                                                      maxSize=self.MAX_SIZE
                                                      )

            is_detect = True if len(faces) else False

            if not is_detect:
                raise FaceDetectorError('Face does not found! Please try another photo')
        except Exception as e:
            raise FaceDetectorError(str(e))
