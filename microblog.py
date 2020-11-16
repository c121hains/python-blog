from app import app, db
from app.models import User, Post
from app import cli

#'Flask shell' calls this make_shell_context()
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}