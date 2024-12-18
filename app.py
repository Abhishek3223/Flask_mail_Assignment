from flask import Flask, render_template, request, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# Configure Flask-Mail using environment variables
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS') == 'True'
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')

mail = Mail(app)

# Route for the form
@app.route("/", methods=["GET", "POST"])
def send_email():
    if request.method == "POST":
        # recipient = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if  not subject or not message:
            flash("All fields are required!", "error")
            return render_template("index.html")

        try:

            recipient = "conversation-7793903_d8e607e637d7ee46df2dc43cfa387a46@remail.wellfound.com"

            msg = Message(subject, recipients=[recipient])
            msg.body = message
            mail.send(msg)
            flash("Email sent successfully!", "success")
        except Exception as e:
            flash(f"Failed to send email. Error: {str(e)}", "error")

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
