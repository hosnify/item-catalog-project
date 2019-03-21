import os
from flask import render_template , flash , redirect , url_for , request ,Blueprint ,current_app
from project2 import db , bcrypt
from project2.users.forms import RegistrationForm , LoginForm , UpdateProfileForm
from project2.users.utils import save_picture
from project2.models import User , OAuth
from flask_login import login_user, current_user, logout_user, login_required
from sqlalchemy.orm.exc import NoResultFound
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.consumer.backend.sqla import SQLAlchemyBackend
from flask_dance.consumer import oauth_authorized
from oauthlib.oauth2.rfc6749.errors import InvalidClientIdError
from project2.config import Config
users= Blueprint('users',__name__)



@users.route('/register', methods =['GET','POST'])
def register():
    """Renders the register page."""
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        form = RegistrationForm()
        if form.validate_on_submit():
            hashed_password= bcrypt.generate_password_hash(form.password.data)
            user = User(user_name = form.user_name.data ,password=hashed_password , email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash(f'account created for {form.user_name.data}', 'success')
            return redirect(url_for('users.login'))
        return render_template(
            'register.html',
            title='Sign Up',
            form= form
        )
@users.route('/login', methods =['GET','POST'])
def login():
    """Renders the login page."""
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user=User.query.filter_by(email=form.email.data).first()
            if user and bcrypt.check_password_hash(user.password , form.password.data):
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('main.home'))
                flash('logged in!', 'success')
            else:
                flash('Login Unsuccessful. Please check email and password', 'danger')
        return render_template('login.html', title='Login', form=form)

        return render_template(
            'login.html',
            title='Sign in',
            form= form
        )

@users.route("/profile", methods =['GET','POST'])
@login_required
def profile():
    """Renders the profile page."""
    form=UpdateProfileForm()
    if form.validate_on_submit():
        if form.profile_image.data:
            picture_file = save_picture(form.profile_image.data)
            current_user.profile_image = picture_file
        current_user.user_name = form.user_name.data
        current_user.email= form.email.data
        db.session.commit()
        flash('changes have been saved', 'success')
    elif request.method=='GET':
        form.user_name.data= current_user.user_name
        form.email.data=current_user.email
    profile_image= url_for('static' , filename='images/'+current_user.profile_image)
    return render_template('profile.html', title='profile', profile_image= profile_image , form=form, user=current_user)


@users.route("/profile/<int:user_id>")
def someone_profile(user_id):
    """Renders profile page for other users ."""
    user = User.query.filter_by(id=user_id).one()
    if current_user.is_authenticated and user==current_user :
        return redirect(url_for('users.profile'))
    profile_image= url_for('static' , filename='images/'+ user.profile_image)
    return render_template('profile.html', title='profile', profile_image= profile_image , user=user)


"""Google Oauth section """

google_blueprint = make_google_blueprint(
    client_id=Config.CLIENT_ID, 
    client_secret=Config.CLIENT_SECRET,
    scope=['https://www.googleapis.com/auth/userinfo.email', 'https://www.googleapis.com/auth/userinfo.profile'] ,
    offline=True
    )

google_blueprint.backend = SQLAlchemyBackend(OAuth, db.session,
                                             user=current_user,
                                             user_required=False)


@users.route("/google_login")
def google_login():
    """redirect to Google to initiate oAuth2.0 """
    if current_user.is_authenticated:
        flash('you are logged in , to switch google account please log out first ', 'success')
        return redirect(url_for('main.home'))
    return redirect(url_for("google.login"))


@oauth_authorized.connect
def google_logged_in(blueprint, token):
    """
    Receives a signal that Google has authenticated User via
    instance of blueprint and token
        1. Check response from instance of blueprint
        2. Check if user exists from db via email
        3. Create user in db if user does not exist
    this require blinker package to run 
    """
    user_info = blueprint.session.get("/oauth2/v2/userinfo")
    if user_info.ok:
        user_info_json = user_info.json()
        email = user_info_json['email']
        query = User.query.filter_by(email=email)

        try:
            user = query.one()
        except NoResultFound:
            user = User()
            user.user_name = user_info_json['name']
            user.email = user_info_json['email']
            db.session.add(user)
            db.session.commit()
        login_user(user, remember=True)

@users.route("/logout")
def logout():
    """ logout user and clear google access_token if exist """
    if google.authorized:
        token = google_blueprint.token["access_token"]
        resp = google.post(
            "https://accounts.google.com/o/oauth2/revoke",
            params={"token": token},
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        logout_user()
        return redirect(url_for('main.home'))
    else :
        logout_user()
        return redirect(url_for('main.home'))


@users.errorhandler(InvalidClientIdError)
def handle_error(error):
    """handle any Client error """
    return redirect(url_for("google.login"))