# -*- coding: utf-8 -*-
#
# HowTo documentation build configuration file, created by
# sphinx-quickstart on Fri Feb 26 10:46:19 2016.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = []
extensions += ['sphinx.ext.imgmath']
extensions += ['sphinx.ext.mathjax']
mathjax_path = 'http://mathjax.connectmv.com/MathJax.js?config=default'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'らぼらいばーの備忘録'
copyright = u'2023, kent'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = 'ja'

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
# pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# import sphinx_rtd_theme  # ( outdated... )
# html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#
# html_theme = 'default'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'nature'
html_theme = "bizstyle"

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
# html_theme_options = {}
# Add any paths that contain custom themes here, relative to this directory.
# html_theme_path = [
#     'content_width': '900px'
# ]

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = 'settings/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']


# -- add by n.k. -- #
# html_css_files = ["custom.css"] -- no effect ?? -- 
# -- "_static/custom.css" will be the optional custum theme. -- #

html_css_files = ["custom.css"]

# def setup(app):
#     app.add_css_file("custom.css")
# -- html_css_files is enough -- #



# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
# html_use_opensearch = 'ja'

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None
html_search_language = "ja"
html_codeblock_linenos_style = "inline"

# Output file base name for HTML help builder.
htmlhelp_basename = 'HowTodoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
    'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
#'preamble': '',
    'fontpkg': r'\usepackage{txfonts}',
    # 'preamble':r'\input{mystyle.tex.txt}'
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'HowTo.tex', u'HowTo Documentation',
   u'kent', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True

# latex document class
latex_docclass = {'manual': 'jsbook'}

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'howto', u'HowTo Documentation',
     [u'kent'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'HowTo', u'HowTo Documentation',
   u'kent', 'HowTo', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'


# -- my arange ---
pngmath_latex_preamble = r'\usepackage{helvet}'
# imgmath_latex_preamble = r'\newcommand{\grad}{ \bvec{ \nabla } }'
# imgmath_latex_preamble = r'\input{source/mystyle.tex.txt}'


sys.path += ['source/settings']
extensions += ['sphinxcontrib_roles']

# configuration case.1: define roles as list (define only roles)
roles = ['strike', 'red', 'redbold', 'blue', 'basictext']

# configuration case.2: define roles as dict (define roles and its style on HTML)
# roles = {'strike': "text-decoration: line-through;",
#          'red': "color: red;",
#          'blue': "color: blue;" }



from sphinx.locale import admonitionlabels
admonitionlabels['note']    = u'Note'
admonitionlabels['warning'] = u'Warning'
