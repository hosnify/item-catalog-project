from project2.models import Category 

def get_all_categories():
    """return all categories in db """
    categories=Category.query.all()
    categories_count = Category.query.count()
    return categories , categories_count