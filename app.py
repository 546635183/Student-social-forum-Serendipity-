from flask import Flask
from exts import db
from models import UserModel
from blueprints.qa import bp as qa_bp
from blueprints.author import bp as author_bp
import config

app = Flask(__name__)
# bind config.py
app.config.from_object(config)

db.init_app(app)

app.register_blueprint(qa_bp)
app.register_blueprint(author_bp)


@app.route('/')
def hello_world():
    return "hello world"


if __name__ == '__main__':
    app.run()
