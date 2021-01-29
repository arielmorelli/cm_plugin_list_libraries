# Plugin Hello for Circulation Manager

This is just a POC for running plugins in [Circulation Manager](https://github.com/NYPL-Simplified/circulation)

# Plugin changes

* new route `/libraries` in CM API returning a list of available libraries.
* Script to list in output all libraries

# Upload to a PyPI server

# Upload to a PyPI server

To upload a package twine is used.
`pip install twine`

1. Build the package
`python setup.py sdist bdist_wheel`

2. Upload to a PyPI server
`twine upload --repository-url <pypi_server_name> dist/*`

Note: To use a local pypi server, please follow [this tutorial](https://github.com/arielmorelli/dev_env_for_circulation/tree/main/plugins)

# Installing the plugin

Please use `pip install -U --index-url <pypi_server_name> cm-plugin-list-libraries`

# Running tests

Once the plugin needs the server_core packages to run, it's necessary to have it under the core folder.
To to this, clone the server_core:
`git clone https://github.com/arielmorelli/server_core core`

To run tests, just run `nosetests tests/` (don't forget to activate the virtualenv activated and install all requirements packages)

