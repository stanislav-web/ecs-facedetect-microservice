# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""
from modules.image_upload.providers.resize_provider import resize
from .providers import UploadProvider, UploadProviderError
from .providers import ResizeProviderError
from .exceptions import ImageUploaderError


class ImageUploader(UploadProvider):
    """ImageUploader class"""

    def __init__(self):
        """
        Init ImageUploader class
        """

        UploadProvider.__init__(self)

    def process(self, uid, request):
        """
        Upload file by params
        :param uid string user identifier
        :param request ImmutableMultiDict
        :raise ImageUploaderError
        :return: bool
        """

        try:
            original = super().upload(uid, request)
            thumb_sizes = self.config['thumb_sizes'].split('x')
            min_sizes = self.config['min_sizes'].split('x')

            wt, ht = thumb_sizes
            wm, hm = min_sizes

            dirname = self.config['save_path'].format(uid=uid)

            thumbnail = resize(original, wt, ht, dirname, self.config['thumbnail'])
            minify = resize(original, wm, hm, dirname, self.config['minify'])

            return dict({
                'uid' : uid,
                'original': original,
                'thumbnail': thumbnail,
                'minify' : minify
            })
        except (UploadProviderError, ResizeProviderError) as error:
            raise ImageUploaderError(error)
