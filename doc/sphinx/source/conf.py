# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('../../../python'))

# -- Configure Mock modules ---------------------------------------------------

# autodoc_mock_imports = [ 'numpy', 'mbhpy.utils' ]
# from unittest.mock import MagicMock

# class Mock(MagicMock):
#     @classmethod
#     def __getattr__(cls, name):
#         return MagicMock()

# MOCK_MODULES = [ 'numpy', '.utils' ]
# sys.modules.update((mod_name, Mock()) for mod_name in MOCK_MODULES)

# -- Configuration for ReadTheDocs setup -------------------------------------

import subprocess
 
def configureDoxyfile(input_dir, output_dir):
    with open('../../doxyfile.in', 'r') as file :
        filedata = file.read()
 
    filedata = filedata.replace('@DOXYGEN_INPUT_DIR@', input_dir)
    filedata = filedata.replace('@DOXYGEN_OUTPUT_DIR@', output_dir)
 
    with open('doxyfile', 'w') as file:
        file.write(filedata)
 
# Check if we're running on Read the Docs' servers
read_the_docs_build = os.environ.get('READTHEDOCS', None) == 'True'
 
breathe_projects = {}
 
if read_the_docs_build:
    input_dir = '../../../mbh'
    output_dir = 'build'
    configureDoxyfile(input_dir, output_dir)
    subprocess.call('doxygen', shell=True)
    breathe_projects['MBH'] = output_dir + '/xml'

# -- Project information -----------------------------------------------------

project = 'MBH'
copyright = '2019, Tommaso Ronconi'
author = 'Tommaso Ronconi'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'breathe',
               'sphinx.ext.autodoc',
               'sphinx.ext.coverage',
               'sphinx.ext.napoleon' ]

# Breathe configuration
breathe_default_project = 'MBH'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

autodoc_mock_imports = [ 'numpy', 'mbhpy.utils' ]

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
