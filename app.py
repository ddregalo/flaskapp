from data import Articles
from flask.ext.pymongo import PyMongo
import bcrypt
from flask import(
    Flask,
    render_template,
    flash,
    url_for,
    session,
    logging,
    redirect
)

Articles = Articles()

def create_app():

    app = Flask(__name__)

    app.config['MONGO_DBNAME'] = 'flaskapp'
    app.config['MONGO_URI'] = 'mongodb://<dbuser>:<dbpassword>@ds217560.mlab.com:17560/flaskapp'

    mongo = PyMongo(app)

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')

    @app.route('/articles')
    def articles():
        return render_template('articles.html', articles = Articles)

    @app.route('/article/<string:id>/')
    def article(id):
        return render_template('article.html', id = id)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
