## Problem statement:

Develop a Flask Blueprint to find the distance from the Moscow's Ring Road to the specified address. The address is passed to the application in an HTTP request, if the specified address is located inside the MKAD, the distance does not need to be calculated. Add the result to the .log file.


## Description

A Flask web app that uses the Yandex Geocoder API to calculate the distance in kilometers from the Moscow Ring Road to a specified destination.


## Tools
- Python 3.8
- Yandex Geocoder API


## Setup
- git clone https://github.com/James-spiff/distance-calculator.git
- pip install -r requirements.txt
- run python main.py
- Press http://127.0.0.1:5000/ to browser
- input destunation

## Docker image
- docker pull jamesonspiff/distance-calculator:1.0
