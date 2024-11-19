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
    
class Entry(db.Model): #Entry models
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    creation_date = db.Column(db.DateTime, nullable=False)
    updated_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', lazy=True))

    user = db.relationship('User', backref=db.backref('entries', lazy=True))


    def to_json(self):
        return{
            "id":self.id,
            "title":self.title,
            "content": self.content,
            "creationDate":self.creation_date,
            "updatedDate":self.updated_date,
            "userId":self.user_id
        }