from flask import Blueprint, render_template, request
from .get_distance import get_distance_with_geocoder

distance = Blueprint('distance', __name__, template_folder='templates')


@distance.route('/distance', methods=['GET', 'POST'])
def index():
	distance = ' '
	if request.method == 'POST':
		location2 = request.form.get('location2')
		if location2 == None:
			return "Input valid location"
		else:
			distance = get_distance_with_geocoder(str(location2))

	return render_template("distance.html", distance=distance)