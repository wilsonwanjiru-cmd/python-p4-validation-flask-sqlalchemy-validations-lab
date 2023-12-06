from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Author, Post

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return 'Validations lab'

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        # Inserting some sample data for testing
        author = Author(name='John Doe', phone_number='1234567890')
        post = Post(title="Sample Post", content="This is a sample post content.", category='Fiction', summary='Sample summary')
        db.session.add(author)
        db.session.add(post)
        db.session.commit()
    app.run(port=5555, debug=True)
