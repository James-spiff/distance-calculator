from flask import Flask
from distance.distance_find import distance 

app = Flask(__name__)
app.register_blueprint(distance, url_prefix="/")

if __name__ == '__main__':
	app.run(debug=True)