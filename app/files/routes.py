# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from app.home import blueprint
from flask import render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import login_manager
from jinja2 import TemplateNotFound

@blueprint.route('/list')
#@login_required
def list():
    return 'Working !!!'

@blueprint.route('/list-html')
#@login_required
def list_html():
    return render_template('list-index.html')
