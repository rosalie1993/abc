from flask import (
	Flask, 
	render_template,
	g
)

import sqlite3

app = Flask(__name__)
app.database= "blog_posts.db"

def connect_db():
	return sqlite3.connect(app.database)

@app.route('/posts')
def posts():
	g.db = connect_db()
	cur = g.db.execute("select * from posts")
	posts = [dict(title=row[0], description=row[1]) for row in cur.fetchall()]
	g.db.close()
	return render_template("posts.html", posts=posts)

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/welcome')
def welcome():
	return "welcome page"

#@app.route('/login', methods=['GET', 'POST'])
#def login():


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html', name=name)

@app.route('/students/')
def students():
	list_of_students = ["Rosalie", "Charlotte"]
	return render_template('students.html', students=list_of_students)


if __name__ == '__main__':
	app.run(debug=True)