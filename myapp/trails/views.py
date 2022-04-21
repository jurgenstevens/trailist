from flask import render_template, url_for, flash, request, redirect, Blueprint, abort
from flask_login import current_user, login_required
from myapp import db 
from myapp.models import Trail
from myapp.trails.forms import TrailForm

trails = Blueprint('trails', __name__)

# this view route allows us to create a trail
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

# this view route allows us to view a specific trail
@trails.route('/<int:trail_id>')
def show_trail(trail_id):
    trail = Trail.query.get_or_404(trail_id)
    return render_template('trail.html', 
            trail_name=trail.trail_name, 
            distance=trail.distance, 
            review=trail.review, 
            comment=trail.comment, 
            trail_image=trail.trail_image,
            trail=trail)

# this view route will allow us to update a trail
@trails.route('/<int:trail_id>/update',methods=['GET','POST'])
@login_required
def update_trail(trail_id):
    trail = Trail.query.get_or_404(trail_id)
    # make sure that the current author is equal to the current user
    if trail.author != current_user:
        abort(403)

    form = TrailForm()

    if form.validate_on_submit():
        trail.trail_name = form.trail_name.data, 
        trail.distance = form.distance.data, 
        trail.review = form.review.data, 
        trail.comment = form.comment.data, 
        trail.trail_image = form.trail_image.data
        db.session.commit()
        flash('Trail Updated')
        return redirect(url_for('trails.trail',trail_id=trail.id))

    elif request.method == 'GET':
        trail.trail_name = form.trail_name.data, 
        trail.distance = form.distance.data, 
        trail.review = form.review.data, 
        trail.comment = form.comment.data, 
        trail.trail_image = form.trail_image.data

    return render_template('create_post.html',title='Updating',form=form)