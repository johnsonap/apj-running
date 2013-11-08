#!/usr/bin/env python

from flask import Flask, render_template
import requests, os
app = Flask(__name__)


# Map My Run API Key
MMR_API_KEY = os.environ.get('MMR_API_KEY')
MMR_ACCESS_TOKEN = os.environ.get('MMR_ACCESS_TOKEN')
MMR_USER_ID = os.environ.get('MMR_USER_ID')

@app.route('/')
def index():

	workout_url = "https://oauth2-api.mapmyapi.com/v7.0/workout/?user="+MMR_USER_ID+"&access_token="+MMR_ACCESS_TOKEN
	workout_headers = {
	    "Api-Key": MMR_API_KEY,
	    "Authorization": "Bearer "+MMR_ACCESS_TOKEN
	}
	r = requests.get(workout_url,headers=workout_headers)
	workouts = dict()
	workouts = r.text

	return render_template('index.html', workouts = workouts)

if __name__ == '__main__':
    app.run(debug=True)