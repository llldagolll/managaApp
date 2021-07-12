from datetime import datetime
from app.lib.db import db
import logging
import sys

logger = logging.getLogger(__name__)

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text())
    content = db.Column(db.Text())
