from config import db, bcrypt, jwt


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False) #max username length of 80 and unique usernames
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)

    def to_json(self):
        return {
            "id": self.id,
            "username":self.username,
            "email":self.email,
        }
    