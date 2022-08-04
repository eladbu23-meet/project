from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

config={

  "apiKey": "AIzaSyDkii4lEXz3O7DroDVA2yV5jLW4sCMV860",

  "authDomain": "mini-cs-project.firebaseapp.com",

  "projectId": "mini-cs-project",

  "storageBucket": "mini-cs-project.appspot.com",

  "messagingSenderId": "928009016811",

  "appId": "1:928009016811:web:3832dbdaea6cd9a8a135ae",

  "measurementId": "G-X3GHRT8GQ9",

  "databaseURL": "https://mini-cs-project-default-rtdb.europe-west1.firebasedatabase.app"
}
    
    

firebase=pyrebase.initialize_app(config)
auth=firebase.auth()   
db = firebase.database() 

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/home')
def home():
    username=db.child("Users").child(login_session['user']['localId']).child("user").get().val()
    return render_template('index.html',username=username)

@app.route('/product')
def proudcte():
  return render_template('product-details.html')


@app.route('/cart')
def cart21():
  return render_template('cart.html')
@app.route('/br')
def br2():
  return render_template('br.html')
@app.route('/bl')
def bl2():
  return render_template('bl.html')
@app.route('/dg')
def dg21():
  return render_template('dg.html')


@app.route('/', methods =['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pswd']
        try:
            login_session['user'] = auth.sign_in_with_email_and_password(email, password)
            return redirect(url_for('home'))
        except:
            print("Error")
    else:
        return render_template("login.html")

@app.route('/signup', methods = ["GET", "POST"])
def signup():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['pswd']
        username = request.form['txt']

        try:
            login_session['user'] = auth.create_user_with_email_and_password(email, password)
            user = {"email":email, "password":password, "user":username}
            db.child("Users").child(login_session['user']['localId']).set(user)
            return redirect(url_for('login'))
        except:
            print("error")
    return render_template('login.html')




        


if __name__ == '__main__':
    app.run(debug=True)