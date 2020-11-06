import os
import secrets
from PIL import Image
from flask import Flask, render_template, url_for, flash, redirect, request
from Flask101_07 import app, db, bcrypt, login_manager
from Flask101_07.forms import form_registrasi, form_login, form_perbaruiakun
from Flask101_07.models import user, post
from flask_login import login_user, logout_user, current_user, login_required

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

@app.route("/tentang",)
def tentang():
    return render_template("about1.0.html", title="tentang")

@app.route("/tentang/pengembang")
def pengembang():
    return render_template("aboutcreator1.0.html", title="tentang/pengembang")

@app.route("/daftar", methods = ["GET", "POST"])
def daftar():
    if current_user.is_authenticated:
        return redirect(url_for("beranda"))
    daftar = form_registrasi()
    if daftar.validate_on_submit():
        password_enkripsi = bcrypt.generate_password_hash(daftar.password.data).decode("utf-8")
        pengguna_baru = user(username=daftar.username.data, email=daftar.email.data, password=password_enkripsi)
        db.session.add(pengguna_baru)
        db.session.commit()
        flash(f"Akun {daftar.username.data} berhasil dibuat! Silakan masuk untuk lanjut.", "success")
        logout_user()
        return redirect(url_for("masuk"))
    return render_template("register1.0.html", title="daftar", form = daftar)

@app.route("/masuk", methods = ["GET", "POST"])
def masuk():
    if current_user.is_authenticated:
        return redirect(url_for("beranda"))
    masuk = form_login()
    if masuk.validate_on_submit():
        user_tersedia = user.query.filter_by(email=masuk.email.data).first()
        if user_tersedia and bcrypt.check_password_hash(user_tersedia.password, masuk.password.data):
            login_user(user_tersedia, remember=masuk.remember_account.data)
            lanjut = request.args.get("next")
            flash(f"Selamat datang {current_user.username}!", "success")
            return redirect(lanjut) if lanjut else redirect(url_for("beranda"))
        else:
            flash("Tidak dapat masuk, silakan cek kembali email dan password Anda!", "danger")
    return render_template("login1.0.html", title="masuk", form = masuk)

@app.route("/keluar")
def keluar():
    logout_user()
    return redirect(url_for("masuk"))


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(app.root_path, 'static/profile_pics', picture_fn)

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path)

    return picture_fn

@app.route("/akun", methods=["GET", "POST"])
@login_required
def akun():
    perbarui = form_perbaruiakun()
    if perbarui.validate_on_submit():
        if perbarui.picture.data:
            picture_file = save_picture(perbarui.picture.data)
            current_user.image_file = picture_file
        current_user.username = perbarui.username.data
        current_user.email = perbarui.email.data
        db.session.commit()
        flash("Akun berhasil diperbarui!", "success")
        return redirect(url_for('akun'))
    elif request.method == 'GET':
        perbarui.username.data = current_user.username
        perbarui.email.data = current_user.email
    foto_user = url_for("static", filename="gambar/foto user/" + current_user.profile_picture)
    return render_template("account2.0.html", title="akun", fotonya_user=foto_user, form=perbarui)
