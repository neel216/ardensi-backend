'''
Will hold all database connections and functions
For now, holds temp database operations
'''

listings = []
users = []

def addListing(listing):
    listings.append(listing)
    print(listings)

def searchListings(param, val):
    ret = {}
    for listing in listings:
        if listing[param] == val:
            ret[listing['id']] = {
                'id': listing['id'],
                'category': f"{listing['main_category']} - {listing['sub_category']}",
                'title': listing['title'],
                'college': listing['college'],
                'pay': listing['pay'],
                'description': listing['description'],
                'time': '1 minute', # TODO: FINISH THIS
                'seller_first': listing['seller_first'],
                'seller_last': listing['seller_last'],
                'seller_email': listing['seller_email']
            }
    
    return ret

def addUser(user):
    users.append(user)