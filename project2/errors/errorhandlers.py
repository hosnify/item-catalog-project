from flask import Blueprint, render_template

errorhandlers = Blueprint('errorhandlers', __name__)


@errorhandlers.app_errorhandler(404)
def error_404(error,):
    return render_template('error.html' ,error= 404 ), 404


@errorhandlers.app_errorhandler(403)
def error_403(error):
    return render_template('error.html', error= 403 ), 403

@errorhandlers.app_errorhandler(405)
def error_405(error):
    return render_template('error.html', error= 405 ), 405

@errorhandlers.app_errorhandler(400)
def error_400(error):
    return render_template('error.html', error= 400 ), 400

@errorhandlers.app_errorhandler(401)
def error_401(error):
    return render_template('error.html', error= 401 ), 401

@errorhandlers.app_errorhandler(408)
def error_401(error):
    return render_template('error.html', error= 408 ), 408

@errorhandlers.app_errorhandler(500)
def error_500(error):
    return render_template('error.html' , error =500 ), 500