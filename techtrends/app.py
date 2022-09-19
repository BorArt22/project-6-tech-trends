import sqlite3

from flask import Flask, jsonify, json, render_template, request, url_for, redirect, flash
from werkzeug.exceptions import abort

from datetime import datetime
import logging

# Count all database connections
connection_count = 0

# Function to get a database connection.
# This function connects to database with the name `database.db`
def get_db_connection():
    global connection_count
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    connection_count += 1
    return connection

# Function to get a post using its ID
def get_post(post_id):
    connection = get_db_connection()
    post = connection.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    connection.close()
    return post

# Define the Flask application
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'

#Function to log messages
def log_message(message):
    app.logger.info('{time}, {message}'.format(
        time=datetime.now().strftime("%d/%m/%Y, %H:%M:%S"), message=message))

# Healthcheck endpoint
@app.route('/status')
def healthcheck():
    try:
        connection = get_db_connection()
        connection.execute('SELECT * FROM posts').fetchall()
        connection.close()
        response = app.response_class(
                response=json.dumps({"result":"OK - healthy"}),
                status=200,
                mimetype='application/json'
        )

        log_message('Status request successfull')
        return response

    except Exception:
        response = app.response_class(
            response=json.dumps({"result":"ERROR - unhealthy"}),
            status=500,
            mimetype='application/json'
        )
        
        log_message('Status request unsuccessfull - ERROR')
        return response

# Metrics endpoint
@app.route('/metrics')
def metrics():
    connection = get_db_connection()
    post_count = connection.execute('SELECT count(1) from posts').fetchone()[0]
    connection.close()
    response = app.response_class(
        response=json.dumps({
            'post_count': post_count,
            'db_connection_count': connection_count
        }),
        status=200,
        mimetype='application/json'
    )

    log_message('[metrics] request')
    return response


# Define the main route of the web application 
@app.route('/')
def index():
    connection = get_db_connection()
    posts = connection.execute('SELECT * FROM posts').fetchall()
    connection.close()
    log_message('The main route of the web application request')
    return render_template('index.html', posts=posts)

# Define how each individual article is rendered 
# If the post ID is not found a 404 page is shown
@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    if post is None:
        log_message('Article "{post_id}" can not be find'.format(post_id = post_id))
        return render_template('404.html'), 404
    else:
        log_message('Article "{post_id}" retrieved'.format(post_id = post_id))
        return render_template('post.html', post=post)

# Define the About Us page
@app.route('/about')
def about():
    log_message('[about] request')
    return render_template('about.html')

# Define the post creation functionality 
@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            log_message('[create] return error because Title is empty')
            flash('Title is required!')
        else:
            connection = get_db_connection()
            connection.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            connection.commit()
            connection.close()

            log_message('[create] Article "{title}" created'.format(title = title))

            return redirect(url_for('index'))

    return render_template('create.html')

# start the application on port 3111
if __name__ == "__main__":
    ## stream logs to app.log file
    logging.basicConfig(filename='app.log',level=logging.DEBUG)

    app.run(host='0.0.0.0', port='3111')
