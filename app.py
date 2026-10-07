from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("index.html")

@app.route('/about')
def about_us():
    return render_template("aboutus.html")

@app.route('/contact')
def contact_us():
    return render_template("contact.html")

@app.route('/services')
def event_services():
    return render_template("eventservices.html")

@app.route('/register')
def register_user():
    return render_template("register.html")

@app.route('/login')
def login_user():
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)
