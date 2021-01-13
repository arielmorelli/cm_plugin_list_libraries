# Plugin Hello for Circulation Manager

This is just a POC for running plugins in [Circulation Manager](https://github.com/NYPL-Simplified/circulation)

# Plugin changes

* new route `/libraries` in CM API returning a list of available libraries.
* Script to list in output all libraries

# Upload to a PyPI server

`python setup.py sdist upload -r <local_pypi_name>`

Nota: use a private PyPI server like [this](https://hub.docker.com/r/pypiserver/pypiserve).

For more informations how configure a Pypi serve, import and install plugins, follow this [link](https://github.com/arielmorelli/dev_env_for_circulation/tree/main/plugins).
