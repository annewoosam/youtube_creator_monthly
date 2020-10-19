"""Script to seed database."""

import os

import json

from datetime import datetime

import crud

import model

import server


os.system('dropdb youtube_creator_monthly')

os.system('createdb youtube_creator_monthly')

model.connect_to_db(server.app)

model.db.create_all()


# Create creator table's initial data.

with open('data/creator.json') as f:

    creator_data = json.loads(f.read())

creator_in_db = []

for creator in creator_data:
    channel_name, email_date, creator_since, month_end_at, number_subscribers, subscribers, views, minutes_watched, likes, comments, posts, shares= (
                                   creator['channel_name'],
                                   creator['email_date'],
                                   creator['creator_since'],
                                   creator['month_end_at'],
                                   creator['number_subscribers'],
                                   creator['subscribers'],
                                   creator['views'],
                                   creator['minutes_watched'],
                                   creator['likes'],
                                   creator['comments'],
                                   creator['posts'],
                                   creator['shares'])

    db_creator = crud.create_creator(
                                 channel_name,
                                 email_date,
                                 creator_since,
                                 month_end_at,
                                 number_subscribers,
                                 subscribers,
                                 views,
                                 minutes_watched,
                                 likes,
                                 comments,
                                 posts,
                                 shares)

    creator_in_db.append(db_creator)

