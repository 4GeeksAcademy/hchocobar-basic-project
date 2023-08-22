from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(20), unique=False, nullable=False)
    name = db.Column(db.String(60), unique=False, nullable=False)
    phone = db.Column(db.String(15), unique=False)
    # Relationship
    # post = db.relationship("Post", backref="user", lazy=True)
    # follower = db.relationship('User', secondary=follower)  # Favoritos

    def __repr__(self):
        return f'<User: {self.email}>'

    def serialize(self):
        return {"id": self.id,
                "email": self.email,
                "name": self.name,
                "phone": self.phone}


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    body = db.Column(db.String(1000), unique=False, nullable=False)
    #  ForeignKey & relationship
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # model.primary_key
    user = db.relationship('User')  # Model name

    def __repr__(self):
        return f'<Post: {self.title} | Author: {self.user_id}>'

    def serialize(self):
        return {"id": self.id,
                "title": self.title,
                "body": self.body,
                "user_id": self.user_id}


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    body = db.Column(db.String(1000), unique=False, nullable=False)
    #  ForeignKey & relationship with User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)  # model.primary_key
    user = db.relationship('User')  # Model name
    #  ForeignKey & relationship with User
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)  # model.primary_key
    post = db.relationship('Post')  # Model name

    def __repr__(self):
        return f'<Comment: {self.title} | Post: {self.post_id} | Author: {self.user_id}>'

    def serialize(self):
        return {"id": self.id,
                "title": self.title,
                "body": self.body,
                "post_id": self.post_id,
                "user_id": self.user_id}


class Follower(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.ForeignKey('user.id')),
    user = db.relationship('User')  # Model name
    follower_id = db.Column(db.ForeignKey('user.id'))
    follower = db.relationship('User')  # Model name

    def __repr__(self):
        return f'<User: {self.user_id} | Follower: {self.follower_id}>'

    def serialize(self):
        return {"id": self.id,
                "user_id": self.user_id,
                "follower_id": self.follower_id}
