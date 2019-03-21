
from flask import render_template ,Blueprint , current_app
from project2.categories.utils import get_all_categories
from project2.courses.utils import get_all_courses 


main= Blueprint('main',__name__)


@main.route('/')
@main.route('/catalog')
@main.route('/home')
def home():
    categories,categories_count= get_all_categories()
    courses,courses_count = get_all_courses()
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        categories=categories,
        categories_count=categories_count ,
        courses=courses,
        courses_count=courses_count
    )