from data import Articles
from flask_pymongo import PyMongo
import bcrypt
import os
from flask import(
    Flask,
    render_template,
    flash,
    url_for,
    session,
    logging,
    redirect,
    request
)

Articles = Articles()
app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'flaskapp'
app.config['MONGO_URI'] = 'mongodb://ddregalo:flaskapp@ds217560.mlab.com:17560/flaskapp'

mongo = PyMongo(app)

def create_app():

    @app.route('/')
    def index():
        if 'username' in session:
            return render_template('home.html')
        return redirect('/login')


    @app.route('/login')
    def login():
        return render_template('login.html')

    @app.route('/register', methods=['POST', 'GET'])
    def register():
        if request.method == 'POST':
            users = mongo.db.users
            existing_user = users.find_one({'name': request.form['username']})
            if existing_user is None:
                # Encrypt user password with bcrypt
                hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'), bcrypt.gensalt())
                users.insert_one({
                    'name': request.form['password'],
                    'password': hashpass
                })
                session['username'] = request.form['username']
                return redirect('/')
            return 'That username already exists.'
        return render_template('register.html')

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
    app.secret_key = 'mysecret'
    app.run(debug=True)
