from flask import * # type: ignore
from markupsafe import escape # type: ignore

app = Flask(__name__)

@app.route('/')
def index():
    # All the routes are defined in the main.py file
    html = """
    <h1>Index</h1>
    <ul>
        <li><a href="/hello">Hello</a></li>
        <li><a href="/user/username">User</a></li>
        <li><a href="/post/1">Post</a></li>
        <li><a href="/path/subpath">Path</a></li>
        <li><a href="/login">Login</a></li>
    </ul>
    """
    return html

@app.route('/hello')
def hello():
    return 'Hello, World'

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'
@app.route('/login', methods=['GET', 'POST'])
def login():
    abort(404)