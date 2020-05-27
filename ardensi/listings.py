'''
API functions for listing related actions
'''
from flask import request, jsonify, abort
from uuid import uuid4
from datetime import datetime

from ardensi.application import app


@app.route('/listing.create', methods=['POST'])
def create():
    req = request.json

    seller_id = req['seller']['user_id']
    seller_email = req['seller']['college']

    main_cat = req['category']['main']
    sub_cat = req['category']['sub']

    title = req['body']['title']
    description = req['body']['description']
    pay = req['body']['pay']

    # generate listing creation timestamp for time_created
    # generate listing uuid number

    # add listing to db with buyer_user_id being null/None/empty

    # return positive response

@app.route('/listing.buy', methods=['POST'])
def buy():
    req = request.json

    listing_id = req['listing_id']
    buyer_id = req['buyer']['user_id']

    # edit buyer_user_id on listing of listing_id to include the buyer's user_id

    # return positive response

@app.route('/listing.temp', methods=['POST'])
def temp():
    req = request.json

    search_param = req['search']['param'] # college, title, main_cat, sub_cat
    search_val = req['search']['val'] # value of search param

    ret = {'13453234': {'id': '13453234',
                        'category': 'Miscellaneous - Music',
                        'title': 'Looking for Piano Teacher',
                        'college': 'UNC-Chapel Hill',
                        'pay': '7/hr',
                        'description': 'Looking for a piano teacher who can meet once a week and teach beginners. Right now, just looking to learn basic fundamentals of playing, but am very enthusiastic.',
                        'time': '2 hours',
                        'seller_first': 'Robert',
                        'seller_last': 'Dimitrov',
                        'seller_email': 'robertd223@unc.edu'
                        },
            '13545687': {'id': '13545687',
                        'category': 'Tutoring - Computer Science',
                        'title': 'Computer Science Tutor Needed',
                        'college': 'UNC-Chapel Hill',
                        'pay': '8/hr',
                        'description': 'Looking for a computer science tutor who can assist with lessons relating to COMP 116. Specifically looking for guidance with data structures and object oriented programming in Python.',
                        'time': '1 day',
                        'seller_first': 'Robert',
                        'seller_last': 'Dimitrov',
                        'seller_email': 'robertd223@unc.edu'
                        }
    }

    return jsonify(ret), 200
    

@app.route('/listing.search', methods=['POST'])
def search():
    req = request.json

    search_param = req['search']['param'] # college, title, main_cat, sub_cat
    search_val = req['search']['val'] # value of search param

    # search listing db for listings that satisfy search parameter and value and return them
    ret = {'13453234': {'id': '13453234',
                        'category': 'Miscellaneous - Textbooks',
                        'title': 'Selling COMP 283 Textbook',
                        'college': 'UNC-Chapel Hill',
                        'pay': '70',
                        'description': 'Selling used textbook for COMP 286: Discrete Structures. Textbook is in good condition, negligible wear. Paperback copy of Discrete Mathematics with Applications, 4th Edition, by Susanna S. Epp.',
                        'time': '28 minutes',
                        'seller_first': 'Neel',
                        'seller_last': 'Runton',
                        'seller_email': 'neelr216@unc.edu'
                        },
            '13545687': {'id': '13545687',
                        'category': 'Tutoring - Science',
                        'title': 'Chemistry Tutor Needed',
                        'college': 'UNC-Chapel Hill',
                        'pay': '8/hr',
                        'description': 'Looking for a chemistry tutor who can assist with topics in CHEM 102. Specifically looking for help with chemical equilibria and thermochemistry. Can meet Wednesdays and Fridays.',
                        'time': '1 hour',
                        'seller_first': 'Martin',
                        'seller_last': 'Ha',
                        'seller_email': 'mha64@unc.edu'
                        },
            '13587946': {'id': '13587946',
                        'category': 'Business Consulting - Programming',
                        'title': 'Full-Stack Developer Needed',
                        'college': 'UNC-Chapel Hill',
                        'pay': '15/hr',
                        'description': 'Our on-campus startup is in need of a full-stack capable developer who can create our product over 2 months. Must be available at least twice a week for meetings/status updates.',
                        'time': '3 hour',
                        'seller_first': 'David',
                        'seller_last': 'Alexander',
                        'seller_email': 'davida51@unc.edu'
                        },
            '13587456': {'id': '13587456',
                        'category': 'Miscellaneous - Housing',
                        'title': 'Apartment Roommate Opening',
                        'college': 'UNC-Chapel Hill',
                        'pay': '400',
                        'description': 'Looking for a male roommate who can pay $400 rent each month. Apartment is 2 bedroom, 2 bath, with a kitchen and living area. Located right next to UNC and access to pool.',
                        'time': '3 days',
                        'seller_first': 'Neel',
                        'seller_last': 'Runton',
                        'seller_email': 'neelr216@unc.edu'
                        }
    }
    # return positive response and listings that satisfy search query
    return jsonify(ret), 200