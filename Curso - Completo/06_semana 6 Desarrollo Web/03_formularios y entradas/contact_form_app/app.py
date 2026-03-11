from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email
import csv
import os

app = Flask(__name__)
app.secret_key = 'Your_secret_key'

# File for storing messages
MESSAGES = "mesagges.csv"

def save_message(name, email, message):
    file_exists = os.path.isfile(MESSAGES)

    with open(MESSAGES, "a", newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)

        # Si el archivo no existe, escribimos encabezados
        if not file_exists:
            writer.writerow(["Name", "Email", "Message"])

        writer.writerow([name, email, message])

# Contact Form Class
class ContactForm(FlaskForm):
    name = StringField("Name", render_kw={"placeholder": "Enter your name"}, validators=[DataRequired()])
    email = StringField("Email", render_kw={"placeholder": "Enter your email"}, validators=[DataRequired(), Email()])
    message = TextAreaField("Message", render_kw={"placeholder": "Write your message"}, validators=[DataRequired()])
    submit = SubmitField("Submit")

# Route for contact Form
@app.route("/", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        save_message(form.name.data,form.email.data,form.message.data)
        flash(f"Thank you, {form.name.data}! Your message has been sent.", "success")
        return redirect(url_for('contact'))
    return render_template("contact.html", form=form)

# Success Page
@app.route('/success')
def success():
    return render_template('success.html')

# Run App
if __name__ == "__main__":
    app.run(debug=True)