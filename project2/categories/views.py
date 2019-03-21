
#from datetime import datetime
#import os
from flask import render_template , flash , redirect , url_for , request ,Blueprint , jsonify 
from project2 import db
from project2.categories.forms import CategoryForm
from project2.models import Category ,CategorySchema
from project2.courses.utils import get_category_courses
from project2.categories.utils import get_all_categories
from flask_login import login_user, current_user, login_required

categories= Blueprint('categories',__name__)


@categories.route("/category/add" , methods =['GET','POST'])
@login_required
def add_category():
    """ Render add category page """
    form=CategoryForm()
    if form.validate_on_submit():
        category=Category(name=form.name.data , description=form.description.data , author = current_user)
        db.session.add(category)
        db.session.commit()
        flash(f'{form.name.data} category has been added successfully' , category='success')
        redirect(url_for('main.home'))
    return render_template('add_category.html', title='add new category', form=form ,legend='create category')


@categories.route("/category/<int:category_id>")
def get_category(category_id):
    """ Render index page to return courses of specific category """
    categories,categories_count= get_all_categories()
    category=Category.query.get_or_404(category_id)
    courses,courses_count =get_category_courses(category)
    return render_template(
        'index.html',
        title= category.name,
        category=category,
        categories=categories,
        categories_count=categories_count,
        courses=courses,
        courses_count=courses_count
    )


@categories.route("/category/<int:category_id>/update", methods=['GET', 'POST'])
@login_required
def update_category(category_id):
    """ Render update category page """
    category = Category.query.get_or_404(category_id)
    if category.author != current_user:
        abort(403)
    form = CategoryForm()
    if form.validate_on_submit():
        category.name = form.name.data
        category.description = form.description.data
        db.session.commit()
        flash('Your category has been updated', 'success')
        return redirect(url_for('categories.get_category', category_id=category.id))
    elif request.method == 'GET':
        form.name.data = category.name
        form.description.data = category.description
    return render_template('add_category.html', title='Update category',
                           form=form, legend='Update category')


@categories.route("/category/<int:category_id>/delete", methods=['POST'])
@login_required
def delete_category(category_id):
    """ Render delete category page """
    category = Category.query.get_or_404(category_id)
    if category.author != current_user:
        abort(403)
    db.session.delete(category)
    db.session.commit()
    flash('Your category has been deleted!', 'success')
    return redirect(url_for('main.home'))

    

@categories.route("/catalog.json")
@categories.route("/categories.json")
def all_categories_json():
    """ implement JSON endpoint for all categories """
    categories=Category.query.all()
    category_schema= CategorySchema(many=True)
    json_data=category_schema.dump(categories).data
    return jsonify(json_data)


@categories.route("/category/<int:category_id>.json")
def get_category_json(category_id):
    """ implement JSON endpoint for specific category """
    category=Category.query.get_or_404(category_id)
    category_schema= CategorySchema()
    json_data=category_schema.dump(category).data
    return jsonify(json_data)