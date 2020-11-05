from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError 
from Flask101_07.models import user

class form_registrasi(FlaskForm):
    username          = StringField("Nama",
                                     validators = [DataRequired(), Length(min=4, max=30)])
    email             = StringField("Email",
                                     validators = [DataRequired(), Email()])
    password          = PasswordField("Password",
                                       validators = [DataRequired()])
    confirm_password  = PasswordField("Konfirmasi password",
                                       validators = [DataRequired(), EqualTo("password")])
    submit            = SubmitField("Daftar")

    def validate_username(self, username_baru):
        kesamaan = user.query.filter_by(username=username_baru.data).first()
        if kesamaan:
            raise ValidationError("Username sudah terpakai, silakan coba username lain")

    def validate_email(self, email_baru):
        kesamaan = user.query.filter_by(email=email_baru.data).first()
        if kesamaan:
            raise ValidationError("Email sudah terpakai, silakan coba email lain")

class form_login(FlaskForm):
    email             = StringField("Email",
                                     validators = [DataRequired(), Email()])
    password          = PasswordField("Password",
                                       validators = [DataRequired()])
    remember_account  = BooleanField("Ingat saya")
    submit            = SubmitField("Masuk")
