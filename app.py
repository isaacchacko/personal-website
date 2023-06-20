from flask import Flask
from views import views

# https://www.youtube.com/watch?v=kng-mJJby8g&ab_channel=TechWithTim

app = Flask(__name__)
app.register_blueprint(views, url_prefix='/')

if __name__ == '__main__':
	app.run(debug=True, port = 8000)