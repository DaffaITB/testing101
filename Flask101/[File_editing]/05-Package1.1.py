from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import form_registrasi, form_login
from models import user, post

app = Flask(__name__)
app.config["SECRET_KEY"] = "thisismysecretkey101"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)

data_post = [
    {
        "Judul"     : "Postingan pertama ku",
        "Nama"      : "Muhammad Daffa Rasyid",
        "Isi"       : "Saat ini aku sedang mengerjakan tugas PengKom",
        "Tanggal"   : "28 Oktober 2020"
    },
    {
        "Judul"     : "Postingan kedua ku",
        "Nama"      : "Ancien Heart",
        "Isi"       : "*sedang memainkan tablet*",
        "Tanggal"   : "Tidak diketahui"
    }
]

@app.route("/")
@app.route("/beranda")
def beranda():
    return render_template("home1.0.html", title="beranda", P = data_post)

@app.route("/daftar", methods = ["GET", "POST"])
def daftar():
    daftar = form_registrasi()
    if daftar.validate_on_submit():
        flash(f"Akun {daftar.username.data} berhasil dibuat!", "success")
        return redirect(url_for("beranda"))
    return render_template("register1.0.html", title="daftar", form = daftar)

@app.route("/masuk", methods = ["GET", "POST"])
def masuk():
    masuk = form_login()
    if masuk.validate_on_submit():
        if masuk.email.data == "ancienheart@gmail.com" and masuk.password.data == "ancien26":
            flash("Selamat datang kembali [ceritanya username]!", "success")
            return redirect(url_for("beranda"))
        else:
            flash("Akun tidak terdaftar, silakan cek kembali email dan password Anda!", "danger")
    return render_template("login1.0.html", title="masuk", form = masuk)

@app.route("/tentang",)
def tentang():
    return render_template("about1.0.html", title="tentang")

@app.route("/tentang/pengembang")
def pengembang():
    return render_template("aboutcreator1.0.html", title="tentang/pengembang")

if __name__ == "__main__":
    app.run(debug=True)