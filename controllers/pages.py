#!/usr/bin/env python
from flask import Blueprint, render_template, url_for, redirect

# controller for default / url prefix
pages = Blueprint("pages",__name__,template_folder="templates")

@pages.route("/", methods=["GET"])
def base_route():
    """
    Base route to any page. Currently, aboutme.
    """
    return redirect(url_for("pages.aboutme"))

@pages.route("aboutme", methods=["GET"])
def aboutme():
    """
    aboutme homepage route for the website.
    """
    return render_template("aboutme.html")
    
@pages.route("resume", methods=["GET"])
def resume():
    """
    resume route.
    """
    return render_template("resume.html")
    
@pages.route("links", methods=["GET"])
def links():
    """
    links route.
    """
    return render_template("links.html")