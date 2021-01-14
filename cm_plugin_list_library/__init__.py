from plugin import list_libraries, LibraryScript, LibraryScriptShortName, LibraryScriptId

routes = [
    {"rule": "/libraries", "view_func": list_libraries},
]

scripts = [
    LibraryScript,
    LibraryScriptShortName,
    LibraryScriptId,
]

