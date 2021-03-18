project = "ContentScraper"
copyright = "2021, Jagath Jai Kumar"
author = "Jagath Jai Kumar"

release = "0.1.0"

extensions = ["autoapi.extension"]
templates_path = ["templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"

autoapi_dirs = [
    "../content_scraper",
]
autoapi_keep_files = False
