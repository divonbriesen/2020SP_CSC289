from flask import Blueprint, render_template

from portfolio.db import get_db

bp = Blueprint('admin', __name__, url_prefix='/admin')


@bp.route('/')
def dashboard():
    db = get_db()

    users = db.execute(
        'SELECT email FROM users'
    ).fetchall()

    return render_template('admin/dashboard.html', users=users)