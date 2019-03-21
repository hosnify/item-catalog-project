from project2.models import Course 


def get_all_courses():
    courses=Course.query.all()
    courses_count = Course.query.count()
    return courses , courses_count


def get_category_courses(category):
    courses=Course.query.filter_by(category=category)
    courses_count = courses.count()
    return courses , courses_count