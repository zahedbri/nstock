# -*- coding: utf-8 -*-

from plugin_picture.content_picture import ContentPicture

if False:
    from gluon import current
    response = current.response
    request = current.request
    T = current.T
    from db import db, auth
    from dc import CT_REG

CT_REG.picture = ContentPicture(db, T, response, request, auth)