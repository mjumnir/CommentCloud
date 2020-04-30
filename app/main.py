from flask import request, render_template, send_from_directory, redirect, url_for, flash
from flask_login import current_user, login_required, logout_user
from app import app, login
from . import auth
import os


@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        return "COMMENT CLOUD", 200
    return render_template('login.html')

@app.route('/test_token', methods=['GET'])
@auth.token_required
def test_token():
    return "Good good token ))"

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for("index"))

@app.route('/protected')
@login_required
def protected():
    flash(current_user.id)
    flash(str(auth.get_token()))
    return render_template('success.html')

@login.unauthorized_handler
def unauthorized_handler():
    # return redirect(url_for("index"))
    return "WTF !!"

@app.route('/js/<string:script>')
def rout_js(script):
    return send_from_directory(os.path.join(app.root_path, 'static', 'js'),
                               script)

@app.route('/css/<string:style>')
def rout_css(style):
    return send_from_directory(os.path.join(app.root_path, 'static', 'css'),
                               style)
