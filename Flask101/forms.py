from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class form_registrasi(FlaskForm):
    username          = StringField("Nama",
                                     validators = [DataRequired(), Length(min=4, max=20)])
    email             = StringField("Email",
                                     validators = [DataRequired(), Email()])
    password          = PasswordField("Password",
                                       validators = [DataRequired()])
    confirm_password  = PasswordField("Konfirmasi password",
                                       validators = [DataRequired(), EqualTo("password")])
    submit            = SubmitField("Daftar")

class form_login(FlaskForm):
    email             = StringField("Email",
                                     validators = [DataRequired(), Email()])
    password          = PasswordField("Password",
                                       validators = [DataRequired()])
    remember_account  = BooleanField("Ingat saya")
    submit            = SubmitField("Masuk")