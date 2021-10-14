# Configuration file for the Sphinx documentation builder.
from datetime import datetime

# -- Project information

project = 'Josh Braun'
copyright = '2021, Josh Braun'
author = 'Josh Braun'

now = datetime.now()
release = version = now.strftime("%Y.%m.%d")

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']
html_static_path = ['_static']

# -- Options for HTML output

html_theme = 'sphinx_rtd_theme'
html_logo = "images/Braun_Professional_Photo.png"

# -- Options for EPUB output
epub_show_urls = 'footnote'
