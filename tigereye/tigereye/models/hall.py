from tigereye.models import db, Model

class Hall(db.Model, Model):
    hid = db.Column(db.Integer, primary_key=True)
    cid = db.Column(db.Integer)
    name = db.Column(db.String(64), nullable=False)
    scrren_type = db.Column(db.String(32))
    audio_type = db.Column(db.String(32))
    stats_num = db.Column(db.Integer, default=0, nullable=False)
    status = db.Column(db.Integer, default=0, nullable=False, index=True)
