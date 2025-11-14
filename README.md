# iBridges CLI plugin example

This repository contains an example on how to create your own plugin for the CLI.

## Requirements

You need iBridges >= 1.5.

## Installation

Install this plugin using:

```sh
pip install git+https://github.com/iBridges-for-iRODS/ibridges-cli-plugin-example.git
```

## Usage

After installing the plugin you use the plugin on the command line:

```sh
ibridges info
ibridges info --help
```

or in the shell:

```sh
ibridges shell
irods:home_collection> info
```

## Develop your own plugin

You can clone this repository and adapt it to your needs. You should change the `README`, `pyproject.toml`, and the python files in `ibridgescontrib/info`.

1) Change the package name from `info` to your own package name
2) Adjust the `__init__.py` in the package
3) Adjust `pyproject.toml`:
    - `[project]`:
      - Add your name and your contacts
      - Adjust the description
      - Add more dependencies if necessary
    - Adjust the `[project.urls]`
    - `[project.entry-points."ibridges.shell"]`
      - Rename `info` to a project ID
      - Adjust the python class it points to `ibridgescontrib.YOUR_PACKAGE.YOUR_PY_FILE:YOUR_COMMANDS`
   - `[tool.setuptools_scm]`: write_to = "ibridgescontrib/YOUR_PACKAGE/_version.py" 
