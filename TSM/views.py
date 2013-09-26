from flask import Flask, request, session, g, redirect, url_for, render_template, flash, abort
from TSM import app,db
from tweet import Geocode_Search


@app.route('/')
def main():	
	lat = 34.1844709
	lng = -118.131809
	radius = '0.1km'
	results = Geocode_Search(lat,lng,radius,last_id)
	level = len(results[0])
	last_id = results[1]
	#return render_template('index.html')
	return level

if __name__ == '__main__':
	app.run(debug=True)