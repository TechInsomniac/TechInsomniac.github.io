from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

from flask import jsonify

@app.route('/_get_current_user')
def get_current_user():
    return jsonify(username='g.user.username',
                   email='g.user.email',
                   id='g.user.id')

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id