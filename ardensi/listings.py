'''
API functions for listing related actions
'''
from flask import request, jsonify, abort

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

    # generate listing creation timestamp
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

@app.route('/listing.search', methods=['POST'])
def search():
    req = request.json

    search_param = req['search']['param'] # college, title, main_cat, sub_cat
    search_val = req['search']['val'] # value of search param

    # search listing db for listings that satisfy search parameter and value and return them

    # return positive response and listings that satisfy search query
