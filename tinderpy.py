
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
# Description: Automates tinder functionality.
# Date: 5/22/2018

import sys
import json
import requests


class User:
    """
    
    """
    session = requests.session()

    def __init__(self, token):
        self.x_auth_token = token

    def discovery(self, location=None):
        """
        discovery([location]) => array[]
        
        GETS a new tinder list of matches based on your tinder settings location
        retrieve raw tinder list and populate array with each list item
        api.gotinder.com/recs/core GETS 10 user(s) match objects with all user data for necessary actions like swiping,
        private messaging etc..
        data contains id's, images, distance, age, name etc..
        data is obtained in raw text format, use json.loads to parse it into json format for iterations
        return array json objects
        :return: [10]{}
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
        GETS the logged users data, retrieves a text based format, what's parsed into json format for iteration
        :return: user.json 
        """
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/v2/profile?include=user',
                                   headers={'x-auth-token': self.x_auth_token})
        processed = json.loads(raw.text)
        if processed['meta']['status'] is 200:
            return processed['data']['user']

    def like(self, _id):
        """
        like(_id) => json response
        http request /api.gotinder.com/like/[USER_ID] will perform the Tinder like action (Swipe right) 
        on the user with the passed _id
        :param _id: String
        :return: json
        """
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/like/%s' % _id,
                                   data={'locale': 'en'},
                                   headers={'x-auth-token': self.x_auth_token})
        return json.loads(raw.text)

    def super_like(self, _id):
        raw = self.session.request('POST',
                                   'https://api.gotinder.com/like/{0}/super'.format(_id),
                                   data={'locale': 'en'},
                                   headers={'x-auth-token': self.x_auth_token})
        return json.loads(raw.text)

    def remove_super_like(self, _id):
        raw = self.session.request('DELETE',
                                   'https://api.gotinder.com/like/{0}/super'.format(_id),
                                   data={'locale': 'en'},
                                   headers={'x-auth-token': self.x_auth_token})
        return json.loads(raw.text)

    def dislike(self, _id):
        """
        dislike(_id) => json response
        http request https://api.go.tinder.com/dislike/[USER_ID] will perform the dislike || pass user action 
        on the user with the passed _id
        :param _id: String
        :return: json
        """
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/pass/%s' % _id,
                                   data={'locale': 'en'},
                                   headers={'x-auth-token': self.x_auth_token})
        return json.loads(raw.text)
      
    def matches(self, count=60):
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/v2/matches?count={0}&locale=en'.format(count),
                                   headers={'x-auth-token': self.x_auth_token})
        return json.loads(raw.text)['data']['matches']

    def fast_match(self, count=20):
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/v2/fast-match?count=20&locale=en',
                                   headers={'x-auth-token': self.x_auth_token},
                                   data={'count': count, 'locale': 'en'})
        return json.loads(raw.text)
      
    def message_match(self, match_id, message):
        message_data = {
            'matchId': match_id + self.user()['_id'],  # Composite key 'private chat key'
            'message': message,
            'userId': match_id
        }

        if isinstance(message, str):
            raw = self.session.request('POST',
                                       'https://api.gotinder.com/user/matches/{0}?locale=en'.format(message_data['matchId']),
                                       headers={'x-auth-token': self.x_auth_token},
                                       data=message_data)
            return json.loads(raw.text)

    def delete_match(self, match_id):
        """
        https://api.gotinder.com/user/matches/58184467ae89a221608cc21c5af27f7596aa953f6d0c7e0e?locale=en
        :return:
        """
        raw = self.session.request('DELETE',
                                   'https://api.gotinder.com/user/matches/{0}'.format(match_id),
                                   data={'locale': 'en'},
                                   headers={'x-auth-token': self.x_auth_token})

        return json.loads(raw.text)

    def _id(self):
        return self.user()['_id']

    def name(self):
        return self.user()['name']

    def position(self):
        return self.user()['pos']

    def gender(self):  # gets the gender M/F
        gender = self.user()['gender']
        if gender is 0:  # Male
            return "Male"
        elif gender is 1:  # Female
            return "Female"

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
