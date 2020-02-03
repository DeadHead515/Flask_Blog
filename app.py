from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(30), nullable=False, default = 'N/A')
    #date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    


    def __repr__(self):
        return f'Blog post: {self.id}'

@app.route('/')
def hello_world():
    return render_template('base.html')

@app.route('/posts/')
def blog_p():
    return render_template('posts.html')

if __name__ == '__main__':
    app.run(debug=True)