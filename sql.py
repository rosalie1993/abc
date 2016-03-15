#sql.py - create a sqlite3 table and populate it with data

import sqlite3

with sqlite3.connect("blog_posts.db") as connection:

	#get a curser object used to execute SQL commands
	c = connection.cursor()

	#delete the table if it doesn't exsist
	c.execute('DROP TABLE posts')

	#create the table
	c.execute('CREATE TABLE posts(title TEXT, description TEXT)')

	#insert dummy data into the table
	c.execute('INSERT INTO posts VALUES("Lorem Ispum", "Lorem Ipsum dolor sit amet.")')
	c.execute('INSERT INTO posts VALUES("Ice cream", "I delicious.")')
	c.execute('INSERT INTO posts VALUES("Pizza", "Mmmmm pizza.")')
	c.execute('INSERT INTO posts VALUES("Hello World", "My very first blog post!.")')

print("Created Database!")