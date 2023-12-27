import re
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/handle_post',methods=['POST'])
def handle_post():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        phone = request.form['phone']
        password = request.form['password']

        if not username.isalpha():
            return "Invalid name. Please enter only alphabets."
        if not (phone.isdigit() and len(phone) == 10 and phone.startswith('9') or phone.startswith('8') or phone.startswith('7') or phone.startswith('6')):
            return "Invalid phone number. Please enter a valid Indian phone number."
        if not (re.match(r'^(?=.*[a-zA-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{1,12}$', password)):
            return "Invalid password. Please enter a combination of alpha-numeric and special characters (max 12 characters)."

    
    return render_template('user.html',username=username,Email=email,phone=phone,password=password)




@app.route('/about/<username>')
def about(username):
    return f"<h1> about Page of the { username }<h1>"