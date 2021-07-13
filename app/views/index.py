from flask import Blueprint
from flask import Flask, request, render_template
# from sqlalchemy import Column, String, Text, Datetime,Integer
from flask_sqlalchemy import SQLAlchemy
from flaskext.markdown import Markdown
from app.models.post import Post
import logging


#export FLASK_APP=app.py
#flask run あるいは python -m flask run

#app = Flask(__name__)
app = Blueprint('index', __name__, url_prefix='/')
#Markdown(app)

#db_uri = 'mysql+pymysql://root:nbroot@localhost/memo?charset=utf8'
#app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
## app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#db = SQLAlchemy(app)


#class Post(db.Model):
#    __tablename__ = 'posts'
#    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#    title = db.Column(db.Text())
#    content = db.Column(db.Text())

logger = logging.getLogger(__name__)
post = Post.getPostDict()



@app.route('/')
def list():

    message = 'Hello memo'
    posts = Post.query.all()
    print(posts)


    return render_template('list.html', message = message, posts = posts)

@app.route('/show/<int:id>')
def show_post(id):

    message = 'Your memo ' + str(id)
    post = Post.query.get(id)

    return render_template('show.html', message=message, post=post)

@app.route('/new')
def new_post():
    
    message = 'New memo'
    return render_template('new.html', message=message)

@app.route('/create', methods=['POST'])
def create_post():

   
        
    message = 'Create new memo'

#    new_post = Post()
#    new_post.title = request.form['title']
#    new_post.content = request.form['content']
#    db.session.add(new_post)
#    db.session.commit()

    post = Post.getPostDict()

    post['title'] = request.form['title']
    post['content'] = request.form['content']
   
    Post.registPost(post)


#    post = Post.query.get(new_post.id)

    logger.info('新しいメモを作成しました')


    return render_template('show.html', message=message, post=post)


@app.route('/delete/<int:id>')
def delete_post(id):

    message = 'Delete Your memo ' + str(id)
#    post = Post.query.get(id)
#    db.session.delete(post)
#    db.session.commit()
#


    Post.delete(id)

    posts = Post.query.all()


    return render_template('list.html', message=message, posts=posts)


@app.route('/edit/<int:id>')
def edit_post(id):

    message = 'Edit your memo' + str(id)
    post = Post.query.get(id)

    return render_template('edit.html', message=message,post=post)


@app.route('/update/<int:id>', methods=['POST'])
def update_post(id):

    message = 'Update your memo' + str(id)

#    post = Post.query.get(id)
#    post.title = request.form['title']
#    post.content = request.form['content']
#    db.session.commit()

    post['id'] = id
    post['title'] = request.form['title']
    post['content'] = request.form['content']
    Post.update(post)

    posts = Post.query.get(id)

    return render_template('show.html', message=message, post=posts)
