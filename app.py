from flask import(
    Flask,
    render_template
)

def create_app():

    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('home.html')

    @app.route('/about')
    def about():
        return render_template('about.html')
        
    return app



if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
