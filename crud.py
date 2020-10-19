"""CRUD operations."""

from model import db, Creator, connect_to_db

import datetime


def create_creator(channel_name, email_date, creator_since, month_end_at, number_subscribers, subscribers, views, minutes_watched, likes, comments, posts, shares):
   

    creator = Creator(channel_name=channel_name,
                  email_date=email_date,
                  creator_since=creator_since,    
                  month_end_at=month_end_at,
                  number_subscribers=number_subscribers,
                  subscribers=subscribers,
                  views=views,
                  minutes_watched=minutes_watched,
                  likes=likes,
                  comments=comments,
                  posts=posts,
                  shares=shares)

    db.session.add(creator)

    db.session.commit()

    return creator

def get_creators():
    """Return all rows of creator monthly data."""

    return Creator.query.all()
 
if __name__ == '__main__':
    from server import app
    connect_to_db(app)
