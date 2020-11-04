class user(db.Model):
    id              = db.Column(db.Integer, primary_key=True)
    username        = db.Column(db.String(20), nullable=False, unique=True,)
    email           = db.Column(db.String(99), nullable=False, unique=True,)
    password        = db.Column(db.String(50), nullable=False)
    profile_picture = db.Column(db.String(20), nullable=False, default="default.jpg")
    posts           = db.relationship("post", backref="author", lazy=True)

    def __repr__(self):
        return f"user('{self.username}', '{self.email}', '{self.profile_picture}')"

class post(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    Judul   = db.Column(db.String(99), nullable=False)
    Isi     = db.Column(db.Text, nullable=False)
    Tanggal = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False,)

    def __repr__(self):
        return f"user('{self.Judul}', '{self.Tanggal}')"