#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Deprecated Library Documentation build configuration file, created by
# sphinx-quickstart on Wed Jul 19 22:23:11 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.coverage',
    'sphinx.ext.githubpages',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = 'Deprecated'
copyright = '2017, Marcos CARDOSO & Laurent LAPORTE'
author = 'Marcos CARDOSO & Laurent LAPORTE'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The full version, including alpha/beta/rc tags.
release = "1.2.14"
# The short X.Y version.
version = release.rpartition('.')[0]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = []

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# This is required for the alabaster theme
# refs: http://alabaster.readthedocs.io/en/latest/installation.html#sidebars
html_sidebars = {
    '**': [
        'about.html',
        'navigation.html',
        'relations.html',  # needs 'show_related': True theme option to display
        'searchbox.html',
        'donate.html',
    ]
}

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Deprecated-Doc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'Deprecated.tex', 'Deprecated Documentation', 'Marcos CARDOSO and Laurent LAPORTE', 'manual')
]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'deprecated', 'Deprecated Documentation', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        'Deprecated',
        'Deprecated Documentation',
        author,
        'Deprecated',
        'Python @deprecated decorator to deprecate old python classes, functions or methods.',
        'Miscellaneous',
    )
]

# Example configuration for intersphinx: refer to the Python standard library.
intersphinx_mapping = {
    'https://docs.python.org/3/': None,
    'https://wrapt.readthedocs.io/en/latest/': None,
    'http://flask.pocoo.org/docs/1.0/': None,
    'django': ('https://docs.djangoproject.com/en/2.1/', 'https://docs.djangoproject.com/en/2.1/_objects/'),
}

# -- Options for EPub output -------------------------------------------

epub_basename = project
epub_theme = 'epub'
epub_theme_options = {
    # relbar1: If this is true, the relbar1 block is inserted in the epub output, otherwise it is omitted.
    'relbar1': False,
    # footer: If this is true, the footer block is inserted in the epub output, otherwise it is omitted.
    'footer': False,
}
epub_title = "Python Deprecated Library v1.2 Documentation"
epub_description = "Python @deprecated decorator to deprecate old python classes, functions or methods."
epub_author = author
epub_contributor = "Original idea from Leandro REGUEIRO, Patrizio BERTONI, Eric WIESER"
epub_language = language or 'en'
epub_publisher = "www.lulu.com"
epub_copyright = copyright
epub_identifier = "9780244627768"
epub_scheme = 'ISBN'
epub_uid = "BookId"  # dacd6b24-3909-4358-8527-359be2e25777
epub_cover = ('_static/title-page.jpg', '')
