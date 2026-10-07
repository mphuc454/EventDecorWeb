from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():  # put application's code here
    return render_template("main/index.html")

@app.route('/about')
def about_us():
    return render_template("main/aboutus.html")

@app.route('/contact')
def contact_us():
    return render_template("main/contact.html")

@app.route('/services')
def event_services():
    return render_template("main/eventservices.html")

@app.route('/register')
def register_user():
    return render_template("auth/register.html")

@app.route('/login')
def login_user():
    return render_template("auth/login.html")

@app.route('/partner')
def partner_user():
    return render_template("main/partner.html")

@app.route('/detailed-events')
def detailed_events():
    return render_template("main/detailedevents.html")

if __name__ == "__main__":
    app.run(debug=True)
