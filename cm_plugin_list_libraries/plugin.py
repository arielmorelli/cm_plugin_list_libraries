from flask import json

from core.model.library import Library
from core.scripts import Script


class Plugin(object):
    """ List libraries plugin entry point.

    This class represent a plugin and all atributes necessary list libraries in CM Api.

    Attributes:
        FREQUENCY (int, optional): integer represing minimum hours to execute.
        SCRIPTS (list): List of scripts to run in the backend of CM.
        FIELDS (list): List of fields to add in the admin interface of CM.
    """
    FREQUENCY = None # no scripts to run
    SCRIPTS = []
    FIELDS = None # no fields to set

    def __init__(self):
        pass

    def activate(self, app):
        @app.route("/libraries")
        def list_libraries():
             _db = app.manager._db
             libraries = [{
                            "name": lib.name,
                            "short name": lib.short_name,
                            "id": lib.id,
                 } for lib in _db.query(Library).all()
             ]
             return app.response_class(
                 response=json.dumps(libraries),
                 status=200,
                 mimetype="application/json",
             )
        
        @app.route("/libraries_short")
        def list_libraries_short():
             _db = app.manager._db
             libraries = [
                { "short name": lib.short_name,
                } for lib in _db.query(Library).all()
             ]
             return app.response_class(
                 response=json.dumps(libraries),
                 status=200,
                 mimetype="application/json",
             )
    
    def run_scripts(self, plugin_name):
        for script in self.SCRIPTS:
            script().run()

