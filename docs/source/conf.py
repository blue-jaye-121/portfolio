# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Portfolio'
copyright = '2026, Jaye Norman'
author = 'Jaye Norman'
html_title = 'Jaye Norman\'s Portfolio'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx_simplepdf',
    'sphinxcontrib.video',
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'pydata_sphinx_theme'
html_show_sourcelink = False
html_static_path = ['_static']
html_theme_options = {
	"collapse_navigation": True,
	"navbar_end": ["navbar-icon-links"],
}
html_context = {
    "default_mode": "dark"
}
html_sidebars = {
    'academics': [],
    'professional_devel': [], 
    'personal_growth' : []
}
html_css_files = [
    'css/custom.css',
 ]