from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask import session

app = Flask(__name__)
app.secret_key = 'Your_secret_key'

# Database Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Database
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Create Database Tables
with app.app_context():
    db.create_all()

# Registration Route
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        if not username or not email or not password:
            flash('All fields are requiered!','error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)

        try:
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('login'))
        except:
            db.session.rollback()
            flash('Username or Email already exist!','error')

    return render_template('register.html')

# Login Route
@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if not email or not password:
            flash('All fields are required!', 'error')
            return redirect(url_for('login'))

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):
            session['user_id'] = user.id
            return redirect(url_for('profile'))

        else:
            flash('Email or password is incorrect', 'error')
            return redirect(url_for('login'))

    return render_template('login.html')

# Profile Route
@app.route('/profile')
def profile():
    user_id = session.get('user_id')

    if not user_id:
        return redirect(url_for('login'))

    user = User.query.get(user_id)

    return render_template('profile.html', user=user)

# Log Out Route
@app.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)  # elimina el usuario de la sesión
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)