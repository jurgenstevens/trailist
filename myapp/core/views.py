# core/views.py 
from flask import render_template, request, Blueprint
from myapp.models import Trail

core = Blueprint('core', __name__)

@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    trails = Trail.query.order_by(Trail.date.desc()).paginate(page=page, per_page=5)
    return render_template('index.html', trails=trails)

@core.route('/info')
def info():
    return render_template('info.html')