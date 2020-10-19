from flask_sqlalchemy import SQLAlchemy

import datetime

db = SQLAlchemy()

# test_month = Creator(channel_name='WinningCheckers', email_date='2020-01-31',number_subscribers = '1', month_end_at='2019-12-31', subscribers='0', views='1', minutes_watched='2', likes='3', comments='4', posts='5', shares='6')

class Creator(db.Model):
    """A class for creator monthly."""
    
    __tablename__ = 'creators'

    creator_monthly_id = db.Column(db.Integer, autoincrement=True, primary_key=True)

    channel_name = db.Column(db.String)

    creator_since = db.Column(db.Date)

    email_date = db.Column(db.Date)

    number_subscribers = db.Column(db.Integer)

    month_end_at = db.Column(db.Date)

    subscribers = db.Column(db.Integer)

    views = db.Column(db.Integer)

    minutes_watched = db.Column(db.Integer)

    likes = db.Column(db.Integer)

    comments = db.Column(db.Integer)
 
    posts = db.Column(db.Integer)
 
    shares = db.Column(db.Integer)

    def __repr__(self):
        return f'<Creator creator_monthly_id={self.creator_monthly_id} channel_name={self.channel_name}>'

def connect_to_db(flask_app, db_uri='postgresql:///youtube_creator_monthly', echo=True):
   
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
   
    flask_app.config['SQLALCHEMY_ECHO'] = echo
   
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    
    db.init_app(flask_app)

    print('Connected to the db!')

if __name__ == '__main__':

    from server import app

    connect_to_db(app)