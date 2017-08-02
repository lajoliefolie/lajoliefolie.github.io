#!/usr/bin/env python
from flask import Blueprint, render_template, url_for, redirect

# controller for default / url prefix
projects = Blueprint("projects",__name__,template_folder="templates")

@projects.route("/", methods=["GET"])
def base_route():
    """
    Base route to any page. Currently, aboutme.
    """
    return redirect(url_for("pages.links"))