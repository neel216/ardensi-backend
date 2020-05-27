'''
API functions for listing related actions
'''
from flask import request, jsonify, abort
from uuid import uuid4
from datetime import datetime

from ardensi.application import app
from ardensi.database import addListing, searchListings, addUser


@app.route('/listing.create', methods=['POST'])
def create():
    req = request.json

    category = req['body']['category'].split(' - ')
    title = req['body']['title']
    college = req['body']['college']
    description = req['body']['description']
    pay = req['body']['pay']
    payment_type = req['body']['payType']
    seller_first = req['seller']['first']
    seller_last = req['seller']['last']
    seller_email = req['seller']['email']

    listing = {
        'time_created': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'id': str(uuid4()),
        'main_category': category[0],
        'sub_category': category[1],
        'title': title,
        'college': college,
        'pay': f'{pay}{payment_type}',
        'description': description,
        'seller_first': seller_first,
        'seller_last': seller_last,
        'seller_email': seller_email,
        'buyer_first': None,
        'buyer_last': None,
        'buyer_email': None,
        'buyer_college': None
    }

    addListing(listing)

    ret = {
        'message': 'listing created'
    }

    return jsonify(ret), 200

@app.route('/listing.buy', methods=['POST'])
def buy():
    req = request.json

    listing_id = req['listing_id']
    
    buyer_first = req['buyer']['first']
    buyer_last = req['buyer']['last']
    buyer_email = req['buyer']['email']

    # edit buyer_first buyer_last and buyer_email on listing of listing_id to include the buyer's info

    # return positive response    

@app.route('/listing.search', methods=['POST'])
def search():
    req = request.json

    search_param = req['search']['param'] # 'college', 'title', 'main_category', 'sub_category'
    search_val = req['search']['val'] # value of search param

    # search listing db for listings that satisfy search parameter and value and return them
    ret = searchListings(search_param, search_val)

    return jsonify(ret), 200

@app.route('/listing.user', methods=['POST'])
def user():
    req = request.json

    user_first = req['user']['first']
    user_last = req['user']['last']
    user_email = req['user']['email']

    query_type = req['type'] # can be 'available' listings (unsold listings), 'sold' listings, or 'purchased' listings