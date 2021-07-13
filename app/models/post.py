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
        return {'title': '', 'content': ''}

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

    def update(post):

        logger.debug('--- Post update start ---')
        reulst = False
        
        try:
            update_post = db.session.query(Post).filter(Post.id==post['id']).first()


            if post['title'] != None:
                update_post.title = post['title']


            if post['content'] != None:
                update_post.content = post['content']

            logger.info('--- Post update update_post ---')
            #insert into posts(title, content) values(...)
            db.session.add(update_post)
            db.session.commit()
            result = True

        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error('--- Post update exception message:{0}'.format(e.with_traceback(tb)))
            db.session.rollback()


        logger.info('--- Post update end')
        return result


    def delete(id):

        logger.info('--- Post delete start ---')
        result = False


        try:
            delete_post = db.session.query(Post).filter(Post.id==id).first()

            logger.info('--- Post delete record')
            db.session.delete(delete_post)
            db.session.commit()
            result = True

        except Exception as e:
            tb = sys.exc_info()[2]
            logger.error('--- Entry delete message:{0}'.format(e.with_traceback(tb)))
            db.session.rollback()


        logger.debug('--- Post delete end ---')
        return result














