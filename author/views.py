from flask_blog import app
from flask import render_template, redirect, url_for, session, request
from author.form import RegisterForm, LoginForm
from author.models import Author
from author.decorators import login_required
import bcrypt

@app.route("/login", methods=('GET', 'POST'))
def login():
    form = LoginForm()
    error = None
    
    if request.method == 'GET' and request.args.get('next'):
        session['next'] = request.args.get('next', None)
    
    # Verify login details
    if form.validate_on_submit():
        author = Author.query.filter_by(
            username=form.username.data
            ).first()
        if author:
            if bcrypt.hashpw(form.password.data, author.password) == author.password:
                
                # Store session data
                session['username'] = form.username.data
                session['is_author'] = author.is_author
                
                # Redirect to previously attempted page in necessary
                if 'next' in session:
                    next = session.get('next')
                    session.pop('next')
                    return redirect(next)
            else:
                error = "Incorrect username and Password"    
            
            return redirect(url_for('index'))
        else:
            error = "Incorrect username and Password"
        
    return render_template('author/login.html', form=form, error=error)
    
@app.route('/logout')
def logout():
    session.pop('username')
    if session.get('is_author'):
        session.pop('is_author')
    return redirect(url_for('index'))
    
@app.route("/register", methods=("GET","POST"))
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        return redirect(url_for('success'))
    else:
        return render_template('author/register.html', form=form)
    
@app.route("/success")
def success():
     return "Author Registered"
