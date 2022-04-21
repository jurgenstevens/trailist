from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Trail
from myapp.trails.forms import TrailForm

trails = Blueprint('trails', __name__)