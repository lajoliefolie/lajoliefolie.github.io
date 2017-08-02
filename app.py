#!/usr/bin/env python
from flask import Flask, render_template, Blueprint
import os
from controllers.pages import pages
from controllers.projects import projects

app = Flask(__name__)

app.register_blueprint(pages, url_prefix='/')
app.register_blueprint(projects, url_prefix='/projects')

if __name__ == "__main__":
    """
    Starting the application.
    """
    # Starting with these values due to c9.io
    host = os.getenv("IP", "0.0.0.0")
    port = os.getenv("PORT", 8080)
    app.secret_key='your_string' # Oh, hush
    app.run(host, port)