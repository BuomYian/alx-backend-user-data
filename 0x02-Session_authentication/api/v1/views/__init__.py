#!/usr/bin/env python3
"""
Initialize the views blueprint
"""

from api.v1.views.index import *
from api.v1.views.users import *
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')


def import_session_auth_view():
    from api.v1.views.session_auth import create_session_auth_view
    app = create_session_auth_view()
    app_views.register_blueprint(app)


# import and register the session_auth view
import_session_auth_view()
