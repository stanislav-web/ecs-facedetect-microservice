# -*- coding: utf-8 -*-

""" ECS-FACEDETECT-MICROSERVICE

    Copyright (C) 2007 Free Software Foundation, Inc.
    Everyone is permitted to copy and distribute verbatim copies of this license document,
    but changing it is not allowed.

    Development Team: Stanislav WEB
"""

import os
from PIL import Image
from .lib import FileSystem
from .exceptions import ResizeProviderError


def resize(imgsrc, twidth, theight, savepath, name='thumbnail'):
    """
    Resize image

    :param str imgsrc: original image source
    :param int twidth: new image width
    :param int theight: new image height
    :param str savepath: new image save path
    :param str name: image name
    :return: str file name
    """

    twidth = int(twidth)
    theight = int(theight)
    savepath = os.path.realpath(savepath)
    extension = 'jpg'

    try:
        image = Image.open(imgsrc)
        image.thumbnail((twidth, theight), Image.ANTIALIAS)

        FileSystem.makedir(savepath)
        filename = "{0}/{1}.{2}".format(savepath, name, extension)

        if imgsrc.rsplit('.', 1)[1].lower() != extension:
            imagenew = Image.new("RGB", image.size, (255, 255, 255))
            imagenew.paste(image, image)
            imagenew.save(filename, 'JPEG', quality=90)
        else:
            image.save(filename, 'JPEG', quality=90)

        return filename
    except (IOError, Exception) as e:
        raise ResizeProviderError(str(e))
