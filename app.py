#!/usr/bin/env python
#push initial test jaemin
from __future__ import print_function

import flask
from flask import Flask, jsonify

import argparse
import json
import pprint
import requests
import sys
import urllib
import yelp
import snapshots
import githubstats

# Create the application.
APP = flask.Flask(__name__)


@APP.route('/api/v1.0/coffeeshops', methods=['GET'])
def get_coffeeshops():
    """
    Get call for coffee shops.
    Return a JSON Object with coffeeshops
    """
    coffee_shops = yelp.start()
    coffee_shops_json = []
    for i in range(0, 3) :
        coffee_shops_json.append(coffee_shops[i].jsonify())
    return jsonify({'coffeeshops': coffee_shops_json})

@APP.route('/')
def index() :
    """ Displays the index page accessible at
    """
    return flask.render_template('home.html')

@APP.route('/scenic')
def sceniclocations() :
	r1 = requests.get('https://maps.googleapis.com/maps/api/place/textsearch/json?type=park&location=30.267153,-97.7430608&radius=10000&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U')
	json1 = r1.json()

	print(json1)
	try:
		rating1 =  json1["results"][0]["rating"]

	except:
		rating1 = 0

	try:
		rating2 =  json1["results"][1]["rating"]
	except:
		rating2 = 0

	try:
		rating3 =  json1["results"][2]["rating"]
	except:

		rating3 = 0

	name1 = json1["results"][0]["name"]
		#location1 = json1["results"][0]["formatted_address"]
		#location1 = json1["results"][0]["formatted_address"]

	photor1 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + json1['results'][0]['photos'][0]['photo_reference']+ '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U'

	name2 = json1["results"][1]["name"]
		#location2 = json1["results"][1]["formatted_address"]

	photor2 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + json1['results'][1]['photos'][0]['photo_reference']+ '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U'

	name3 = json1["results"][2]["name"]
	#location3 = json1["results"][2]["formatted_address"]
	placeID1 = json1["results"][0]["place_id"]
	placeID2 = json1["results"][1]["place_id"]
	placeID3 = json1["results"][2]["place_id"]


	photor3 = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + json1['results'][2]['photos'][0]['photo_reference']+ '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U'
	return flask.render_template('products.html', name1=name1, placeID1= placeID1, rating1=rating1, photo1=photor1, name2=name2, placeID2=placeID2, rating2=rating2, photo2=photor2, name3=name3, placeID3=placeID3, rating3=rating3, photo3=photor3)

@APP.route('/scenic/<placeID>')
def scenicdetails(placeID):
	r1 = requests.get('https://maps.googleapis.com/maps/api/place/details/json?placeid=' + placeID + '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U')
	json1 = r1.json()
	print(json1)
	name = json1['result']['name']

	address = json1["result"]["formatted_address"]
	rating= json1["result"]["rating"]
	photo = 'https://maps.googleapis.com/maps/api/place/photo?maxwidth=400&photoreference=' + json1['result']['photos'][0]['photo_reference']+ '&key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U'
	src_for_map = "https://www.google.com/maps/embed/place?key=AIzaSyBlOaCDL8ePD3nignTrJN1oViXj_rDx_1U&origin=place_id:" + placeID + "&output=embed"

	return flask.render_template('scenicdetails.html', name=name, address=address, photo=photo, src_for_map=src_for_map, rating=rating)


@APP.route('/templates/snapshotsmain.html')
def snapshotsmain():
    img_list = snapshots.start()
    photo1 = img_list[0]
    photo2 = img_list[1]
    photo3 = img_list[2]
    return flask.render_template('snapshotsmain.html', name1 = photo1.name, name2 = photo2.name, name3 = photo3.name,
                                 title1 = photo1.title, title2 = photo2.title, title3 = photo3.title,
                                 num_favs1 = photo1.num_favorites, num_favs2 = photo2.num_favorites, num_favs3 = photo3.num_favorites,
                                 username1 = photo1.username, username2 = photo2.username, username3 = photo3.username,
                                 url1 = photo1.imageUrl, url2 = photo2.imageUrl, url3 = photo3.imageUrl)

@APP.route('/templates/<coffeeId>')
def coffeeshop(coffeeId) :
    coffee_shop = yelp.get_business(coffeeId)
    return flask.render_template('instance1.html', location = coffee_shop.location, name = coffee_shop.name, phone = coffee_shop.phone, price = coffee_shop.price, rating = coffee_shop.rating)

@APP.route('/templates/coffeeshops.html')
def coffeeshops() :
    coffee_shops = yelp.start()
    return flask.render_template('coffeeshops.html', coffeeId1 = coffee_shops[0].id, name1 = coffee_shops[0].name, location1 = coffee_shops[0].location, price1 = coffee_shops[0].price, rating1 = coffee_shops[0].rating, photo1 = coffee_shops[0].imageUrl,
    name2 = coffee_shops[1].name, coffeeId2 = coffee_shops[1].id, location2 = coffee_shops[1].location, price2 = coffee_shops[1].price, rating2 = coffee_shops[1].rating, photo2 = coffee_shops[1].imageUrl,
    name3 = coffee_shops[2].name, coffeeId3 = coffee_shops[2].id, location3 = coffee_shops[2].location, price3 = coffee_shops[2].price, rating3 = coffee_shops[2].rating, photo3 = coffee_shops[2].imageUrl)


@APP.route('/templates/about.html')
def about():
    # Will change this when a database is used
    if(githubstats.calculated == False):
        githubstats.user_commits()
        githubstats.user_issues()
        githubstats.calculated = True
    total_commits = githubstats.total_commits()
    return flask.render_template('about.html', total_commits = total_commits, issues = githubstats.open_issues, amrutha_commits = githubstats.amrutha[0], sonam_commits = githubstats.sonam[0],
                                 jenni_commits = githubstats.jenni[0], ruchi_commits = githubstats.ruchi[0], jaemin_commits = githubstats.jaemin[0], amrutha_issues = githubstats.amrutha[1],
                                 sonam_issues = githubstats.sonam[1], jenni_issues = githubstats.jenni[1], ruchi_issues = githubstats.ruchi[1], jaemin_issues = githubstats.jaemin[1])

if __name__ == '__main__':
    #APP.debug=True
    APP.run()
