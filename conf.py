import sphinx_rtd_theme

html_theme = "sphinx_rtd_theme"

html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

master_doc = 'index'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.mathjax',
]

# General information about the project.
project = u'Adapting LSST Stack'
copyright = u'2016, James Mullaney'
author = u'James Mullaney'

# The short X.Y version.
version = u'0.1'
# The full version, including alpha/beta/rc tags.
release = u'0.1'

