'''
Will hold all database connections and functions
For now, holds temp database operations
'''
from datetime import datetime

listings = []
users = []


def addListing(listing):
    listings.append(listing)
    print(listings)

def searchListings(param, val):
    ret = {}
    for listing in listings:
        if listing[param] == val:
            time = datetime.strptime(listing['time_created'], '%Y-%m-%d %H:%M:%S')
            deltaSeconds = (datetime.now() - time).total_seconds

            ret[listing['id']] = {
                'id': listing['id'],
                'category': f"{listing['main_category']} - {listing['sub_category']}",
                'title': listing['title'],
                'college': listing['college'],
                'pay': listing['pay'],
                'description': listing['description'],
                'time': parseSeconds(deltaSeconds),
                'seller_first': listing['seller_first'],
                'seller_last': listing['seller_last'],
                'seller_email': listing['seller_email']
            }
    
    return ret

def parseSeconds(seconds):
    deltaDays = int(seconds / 86400)
    seconds -= deltaDays * 86400
    
    if deltaDays != 0:
        return f'{deltaDays} day' if deltaDays == 1 else f'{deltaDays} days'
    else:
        deltaHours = int(seconds / 3600)
        seconds -= deltaHours * 3600

        if deltaHours != 0:
            return f'{deltaHours} hour' if deltaHours == 1 else f'{deltaHours} hours'
        else:
            deltaMinutes = int(seconds / 60)
            if deltaMinutes != 0:
                return f'{deltaMinutes} minute' if deltaMinutes == 1 else f'{deltaMinutes} minutes'
        
    return '0 minutes'

def addUser(user):
    users.append(user)