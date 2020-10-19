"""Server for youtube_monthly_creator app."""

# increased flask

from flask import Flask, render_template

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# created import allowing connection to database

from model import connect_to_db, Creator, db

app = Flask(__name__)

# imported Jinja secret key settings
from jinja2 import StrictUndefined

app.secret_key = "dev"

app.jinja_env.undefined = StrictUndefined

import crud

@app.route('/')

def all_youtubecreatormonthlystats():

    stats=crud.get_creators()

    # channel_name=Creator.query(Creator.channel_name).first()
    
    month_end_at=[q[0] for q in db.session.query(Creator.month_end_at).all()]
    
    number_subscribers=[q[0] for q in db.session.query(Creator.number_subscribers).all()]
    
    subscribers=[q[0] for q in db.session.query(Creator.subscribers).all()]
    
    views=[q[0] for q in db.session.query(Creator.views).all()]
    
    minutes_watched=[q[0] for q in db.session.query(Creator.minutes_watched).all()]
    
    likes=[q[0] for q in db.session.query(Creator.likes).all()]
    
    comments=[q[0] for q in db.session.query(Creator.comments).all()]
    
    posts=[q[0] for q in db.session.query(Creator.posts).all()]
    
    shares=[q[0] for q in db.session.query(Creator.shares).all()]

    return render_template('youtubecreatormonthlystats.html', stats=stats, month_end_at=month_end_at, number_subscribers=number_subscribers, subscribers=subscribers, views=views, minutes_watched=minutes_watched, likes=likes, comments=comments, posts=posts, shares=shares)

if __name__ == '__main__':

# added connection to database

    connect_to_db(app)

# during development

    app.run(host='0.0.0.0', debug=True)

# in production

    #app.run()