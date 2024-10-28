from flask import Flask, request, redirect, url_for, render_template
import os

app = Flask(__name__)

UPLOAD_FOLDER = "C:/UserDetails"
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('pg2.html')

@app.route('/add-profile', methods=['POST'])
def add_profile():
    name = request.form['name']
    email = request.form['email']
    gender = request.form['gender']
    usname = request.form['usname']
    password = request.form['C']

    user_data = f"Name: {name}\nEmail : {email}\nGender: {gender}\nUserName: {usname}\nPassword : {password}\n\n"

    with open(os.path.join(UPLOAD_FOLDER, ''), 'a') as f:
        f.write(user_data)

    return redirect(url_for('profile'))

@app.route('/profile')
def profile():
    return 'Profile Saved!'

if __name__ == '__main__':
    app.run(debug=True)