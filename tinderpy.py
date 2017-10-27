
"""
                                                                                                                                                      
                                                            dddddddd                                                                                  
TTTTTTTTTTTTTTTTTTTTTTT  iiii                               d::::::d                                                                                  
T:::::::::::::::::::::T i::::i                              d::::::d                                                                                  
T:::::::::::::::::::::T  iiii                               d::::::d                                                                                  
T:::::TT:::::::TT:::::T                                     d:::::d                                                                                   
TTTTTT  T:::::T  TTTTTTiiiiiiinnnn  nnnnnnnn        ddddddddd:::::d     eeeeeeeeeeee    rrrrr   rrrrrrrrr   ppppp   pppppppppyyyyyyy           yyyyyyy
        T:::::T        i:::::in:::nn::::::::nn    dd::::::::::::::d   ee::::::::::::ee  r::::rrr:::::::::r  p::::ppp:::::::::py:::::y         y:::::y 
        T:::::T         i::::in::::::::::::::nn  d::::::::::::::::d  e::::::eeeee:::::eer:::::::::::::::::r p:::::::::::::::::py:::::y       y:::::y  
        T:::::T         i::::inn:::::::::::::::nd:::::::ddddd:::::d e::::::e     e:::::err::::::rrrrr::::::rpp::::::ppppp::::::py:::::y     y:::::y   
        T:::::T         i::::i  n:::::nnnn:::::nd::::::d    d:::::d e:::::::eeeee::::::e r:::::r     r:::::r p:::::p     p:::::p y:::::y   y:::::y    
        T:::::T         i::::i  n::::n    n::::nd:::::d     d:::::d e:::::::::::::::::e  r:::::r     rrrrrrr p:::::p     p:::::p  y:::::y y:::::y     
        T:::::T         i::::i  n::::n    n::::nd:::::d     d:::::d e::::::eeeeeeeeeee   r:::::r             p:::::p     p:::::p   y:::::y:::::y      
        T:::::T         i::::i  n::::n    n::::nd:::::d     d:::::d e:::::::e            r:::::r             p:::::p    p::::::p    y:::::::::y       
      TT:::::::TT      i::::::i n::::n    n::::nd::::::ddddd::::::dde::::::::e           r:::::r             p:::::ppppp:::::::p     y:::::::y        
      T:::::::::T      i::::::i n::::n    n::::n d:::::::::::::::::d e::::::::eeeeeeee   r:::::r             p::::::::::::::::p       y:::::y         
      T:::::::::T      i::::::i n::::n    n::::n  d:::::::::ddd::::d  ee:::::::::::::e   r:::::r             p::::::::::::::pp       y:::::y          
      TTTTTTTTTTT      iiiiiiii nnnnnn    nnnnnn   ddddddddd   ddddd    eeeeeeeeeeeeee   rrrrrrr             p::::::pppppppp        y:::::y           
                                                                                                             p:::::p               y:::::y            
                                                                                                             p:::::p              y:::::y             
                                                                                                            p:::::::p            y:::::y              
                                                                                                            p:::::::p           y:::::y               
                                                                                                            p:::::::p          yyyyyyy                
                                                                                                            ppppppppp                                 
    Generated with http://patorjk.com/software/taag/                                                                                                                                                  
"""


# Author: Spencer J Potts
# Description:
#
#
# Date:
# Version: v0.1



import json
import requests


class User:
    """
    
    """
    session = requests.session()

    def __init__(self, token):
        self.x_auth_token = token

    def subjects(self):
        """
        subject([radius, ]) => array[]
        
        Obtain a new tinder list of matches based on your tinder settings location
        retrieve raw tinder list and populate array with each list item
        api.gotinder.com/recs/core GETS 10 user match objects with all user data for necessary actions like swiping,
        private messaging, removing from your matches list etc..
        data contains id's, images, distance, age, name etc..
        one data is obtained in raw format use json.loads to parse it into json format for usage
        return array
        :return: [10]
        """
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/recs/core?locale=en/',
                                   headers={'x-auth-token': self.x_auth_token})
        processed = json.loads(raw.text)
        arr = []
        for user in processed['results']:
            arr.append(user)
        return arr

    def user(self):
        """
        user() => json.object
        Obtains the logged users data, retrieves a text based format, what's parsed into json format for iteration
        :return: user.json 
        """
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/v2/profile?include=user',
                                   headers={'x-auth-token': self.x_auth_token})
        processed = json.loads(raw.text)
        if processed['meta']['status'] is 200:
            return processed['data']['user']

    def like(self, _id):
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/like/%s' % _id,
                                   data={'locale': 'en'},
                                   headers={'x-auth-token': self.x_auth_token})
        return json.loads(raw.text)

    def _id(self):
        return self.user()['_id']

    def name(self):
        return self.user()['name']

    def position(self):
        return self.user()['pos']

    def gender(self):
        return self.user()['gender']

    def age_filter_min(self):
        return self.user()['age_filter_min']

    def age_filter_max(self):
        return self.user()['age_filter_max']

    def birthday(self):
        return self.user()['birth_date']

    def interests(self):
        raw = self.user()['interests']
        arr = []
        for interest in raw:
            arr.append(interest)
        return arr

    def photos(self):
        photos = self.user()['photos']
        arr = []
        for photo in photos:
            arr.append(photo)
        return arr

    def jobs(self):
        jobs = self.user()['jobs']
        arr = []
        for job in jobs:
            arr.append(job)
        return arr

    def schools(self):
        schools = self.user()['schools']
        arr = []
        for school in schools:
            arr.append(school)
        return arr

    def discoverable(self):
        return self.user()['discoverable']
