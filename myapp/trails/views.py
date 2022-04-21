from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Trail
from myapp.trails.forms import TrailForm

trails = Blueprint('trails', __name__)

@trails.route('/create', methods=['GET', 'POST'])
@login_required
def create_trail():
    form = TrailForm()
    if form.validate_on_submit():
        trail = Trail(
            trail_name=form.trail_name.data, 
            distance=form.distance.data, 
            review=form.review.data, 
            comment=form.comment.data, 
            trail_image=form.trail_image.data, 
            user_id=current_user.id)
        db.session.add(trail)
        db.session.commit()
        flash('Trail Created')
        print('Trail was created')
        return redirect(url_for('core.index'))
    return render_template('create_trail.html', form=form)