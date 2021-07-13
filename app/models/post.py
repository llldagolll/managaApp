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


    def __repr__(self):
        return '<Post %r>' % self.title


    def getPostDict():
        return {'title':'', 'content', ''}

    def getPostList():
        #select * from posts
        post_list = db.session.query(Post).all()


        if post_list == None:
            return []
        else:
            return post_list


    def registPost(post):
        
        logger.debug('start to post Memo')
        result = False

        #now_date = datetime.now()
        
        record = Post(
                title = post['title'],
                content = post['content']
                )

        try:
            logger.debug('insert registPost')
            #insert into post(id, content) values(...)
            db.session.add(record)
            db.session.commit()
            result = True

        except Exception as e:
            tb = sys.exec_info()[2]
            logger.error('insert exception registPost message:{0}'.format(e.with_traceback(tb)))
            db.session.rollback()
        return result
