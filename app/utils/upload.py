import secrets
import os
from flask import current_app


def uploadImage(image, path=''):
    random_ex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(image.filename)

    filename = random_ex + f_ext

    image_path = os.path.join(current_app.root_path, 'static/' + path, filename)
    image.save(image_path)

    return path + filename
