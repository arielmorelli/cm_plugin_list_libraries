from flask import json

from core.model.library import Library
from core.scripts import Script


def list_libraries(app):
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

