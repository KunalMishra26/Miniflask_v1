
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thecodex'

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/about")
def about():
    return "The about page"

@app.route("/blog")
def blog():
    posts = [{'title': "How the journey started", "author": "Kunal Mishra"},
             {"title": "How it is going on", "author": "Sachin Thakur"}]
    return render_template('blog.html', author = "Sachin Thakur", sunny = True, posts = posts)

@app.route("/blog/<blogid>")
def blogpost(blogid):
    return "this is blog post number " + str(blogid)