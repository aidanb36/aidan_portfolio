from flask import Flask, render_template, request, url_for, redirect
import smtplib
from email.mime.text import MIMEText
from email.message import EmailMessage

#name
app = Flask(__name__)

#index route
@app.route("/")
def index():
    return render_template("index.html")


#send email
@app.route("/sendemail/", methods=['POST'])
def sendemail():
    if request.method == "POST":
        name = request.form['name']
        subject = request.form['Subject']
        email = request.form['_replyto']
        message = request.form['message']

        # Set your credentials
        yourEmail = "aidanb363@gmail.com"
        yourPassword = "flhvxlxsfqxaayul"

        # Logging in to our email account
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.login(yourEmail, yourPassword)

        # Sender's and Receiver's email address
        msg = EmailMessage()
        msg.set_content("First Name : " + str(name)
                        + "\nEmail : " + str(email)
                        + "\nSubject : " + str(subject)
                        + "\nMessage : " + str(message))
        msg['To'] = email
        msg['From'] = yourEmail
        msg['Subject'] = subject

        # Send the message via our own SMTP server.
        try:
            # sending an email
            server.send_message(msg)
            print("Send")
        except:
            print("Fail to Send")
            pass

    return redirect('/')


#main
if __name__ == "__main__":
    app.run(debug=True)
