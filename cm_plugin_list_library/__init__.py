from plugin import list_libraries, LibraryScript, LibraryScriptShortName, LibraryScriptId

routes = [
    {"rule": "/libraries", "view_func": list_libraries},
]

run_func = [
    {"func": LibraryScript},
    {"func": LibraryScriptShortName},
    {"func": LibraryScriptId},
]

