from flask import json

from core.model.library import Library
from core.scripts import Script


class LibraryScript(Script):
    def run(self):
        libraries = [
            { "name": lib.name,
               "short name": lib.short_name,
               "id": lib.id,
            } for lib in self._db.query(Library).all()
        ]
        print(libraries)


class LibraryScriptShortName(Script):
    def run(self):
        libraries = [
            {
               "short name": lib.short_name,
            } for lib in self._db.query(Library).all()
        ]
        print(libraries)


class LibraryScriptId(Script):
    def run(self):
        libraries = [
            {
               "id": lib.id,
            } for lib in self._db.query(Library).all()
        ]
        print(libraries)


class Plugin(object):
    SCRIPTS = [LibraryScript, LibraryScriptId, LibraryScriptShortName]
    def __init__(self):
        pass

    def activate(self, app):
        @app.route("/libraries")
        def list_libraries():
             _db = app.manager._db
             libraries = [
                 { "name": lib.name,
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
                 {
                     "short name": lib.short_name,
                 } for lib in _db.query(Library).all()
             ]
             return app.response_class(
                 response=json.dumps(libraries),
                 status=200,
                 mimetype="application/json",
             )
    
    def run_scripts(self):
        for script in self.SCRIPTS:
            script.run()

