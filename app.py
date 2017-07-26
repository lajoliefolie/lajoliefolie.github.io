#!/usr/bin/env python
from flask import Flask
import os
from controllers.pages import pages

app = Flask(__name__)

app.register_blueprint(pages, url_prefix='/')

if __name__ == "__main__":
    """
    Starting the application.
    """
    # Starting with these values due to c9.io
    host = os.getenv("IP", "0.0.0.0")
    port = os.getenv("PORT", 8080)
    app.secret_key='your_string' # Oh, hush
    app.run(host, port)