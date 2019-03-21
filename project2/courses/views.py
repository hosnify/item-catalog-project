

from flask import render_template , flash , redirect , url_for , request ,Blueprint , jsonify
from project2 import db 
from project2.courses.forms import courseForm 
from project2.models import Category , Course ,CourseSchema
from flask_login import login_user, current_user, login_required

courses= Blueprint('courses',__name__)


@courses.route("/course/add" , methods =['GET','POST'])
@login_required
def add_course():
    """ Render add course page """
    form=courseForm()
    if form.validate_on_submit():
        course=Course(name=form.name.data , description=form.description.data , author= current_user , category=form.Category.data , price = form.price.data )
        db.session.add(course)
        db.session.commit()
        flash(f'{form.name.data} course has been added successfully' , category='success')
        redirect(url_for('main.home'))

    return render_template('add_course.html', title='add new course', form=form, legend='create course ')



@courses.route("/course/<int:course_id>")
def get_course(course_id):
    """ Render course information page """
    course=Course.query.get_or_404(course_id)
    return render_template('get_course.html', title=course.name, course=course)



    
@courses.route("/course/<int:course_id>/update", methods=['GET', 'POST'])
@login_required
def update_course(course_id):
    """ Render update course page """
    course = Course.query.get_or_404(course_id)
    if course.author != current_user:
        abort(403)
    form = courseForm()
    if form.validate_on_submit():
        course.name = form.name.data
        course.description = form.description.data
        course.price = form.price.data
        db.session.commit()
        flash('Your course has been updated', 'success')
        return redirect(url_for('courses.get_course', course_id=course.id))
    elif request.method == 'GET':
        form.name.data = course.name
        form.description.data = course.description
        form.price.data = course.price

    return render_template('add_course.html', title='Update course',
                           form=form, legend='Update course')


@courses.route("/course/<int:course_id>/delete", methods=['POST'])
@login_required
def delete_course(course_id):
    """ Render delete course page """
    course = Course.query.get_or_404(course_id)
    if course.author != current_user:
        abort(403)
    db.session.delete(course)
    db.session.commit()
    flash('Your course has been deleted!', 'success')
    return redirect(url_for('main.home'))



@courses.route("/courses.json")
def all_courses_json():
    """ implement JSON endpoint for all courses """
    courses=Course.query.all()
    category_schema= CourseSchema(many=True)
    json_data=category_schema.dump(courses).data
    return jsonify(json_data)


@courses.route("/course/<int:course_id>.json")
def get_course_json(course_id):
    """ implement JSON endpoint for specific course """
    course=Course.query.get_or_404(course_id)
    course_schema= CourseSchema()
    json_data=course_schema.dump(course).data
    return jsonify(json_data)