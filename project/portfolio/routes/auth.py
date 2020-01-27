import functools

from flask import Blueprint, request, render_template, redirect, url_for, flash, g, session
from werkzeug.security import check_password_hash, generate_password_hash

from portfolio.db import get_db

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/register', methods=('GET', 'POST'))
def register():
    if request.method == 'POST':

        # email/password error checking
        email = request.form['email']
        password = request.form['password']
        db = get_db()

        error = None

        if not email:
            error = 'Email is required'
        elif not password:
            error = 'Password is required'
        elif db.execute(
            'SELECT id FROM users WHERE email = ?', (email,)
        ).fetchone() is not None:
            error = f'{email} is already registered'

        if error is None:
            print('No errors')

            hashed_password = generate_password_hash(password)
            # add user to the database
            db.execute('INSERT INTO users (email, password) VALUES (? , ?)',
                       (email, hashed_password)
            )
            db.commit()

            # redirect to login page
            return redirect(url_for('auth.login'))

        # display any errors
        print(error)
        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':

        email = request.form['email']
        password = request.form['password']
        db = get_db()

        error = None

        # query database for email
        user = db.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()

        if user is None:
            error = 'Incorrect email address'

        # test password against stored password hash
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password'

        if error is None:
            session.clear()

            # create a new user session
            session['user_id'] = user['id']

            # redirect to homepage
            return redirect(url_for('index'))

        # display any errors
        flash(error)

    return render_template('auth/login.html')


@bp.before_app_request
def load_logged_in_user():
    # get the user session
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        db = get_db()
        # query the database for the user_id
        g.user = db.execute(
            'SELECT * FROM users WHERE id = ?', (user_id,)
        ).fetchone()


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
