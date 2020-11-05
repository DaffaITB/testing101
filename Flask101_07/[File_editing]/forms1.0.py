from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 
from Flask101.models import user

# Nama  = Muhammad Daffa Rasyid
# NIM   = 16520147


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

    def validate_username(self, username_baru):
        kesamaan = user.query.filter_by(username_baru=username.data).first()
        if kesamaan:
            raise ValidationError("{daftar.username.data} sudah terpakai, silakan coba username lain")

    def validate_username(self, email_baru):
        kesamaan = user.query.filter_by(email_baru=username.data).first()
        if kesamaan:
            raise ValidationError("{daftar.email.data} sudah terpakai, silakan coba email lain")

class form_login(FlaskForm):
    email             = StringField("Email",
                                     validators = [DataRequired(), Email()])
    password          = PasswordField("Password",
                                       validators = [DataRequired()])
    remember_account  = BooleanField("Ingat saya")
    submit            = SubmitField("Masuk")