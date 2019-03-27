
"""
    @Author: Spencer J Potts
    @Description: Automates tinder functionality.
    @Date: 

"""

import sys
import json
import requests

from .profile import Profile
from .match import Match


class User:
    """
    
    """
    BASE_ADDRESS = 'https://api.gotinder.com'
    
    def __init__(self, token):
        self.session = requests.session()
        self.x_auth_token = token
        self.headers = {'x-auth-token': token}
        

    def discovery(self):
        """
        discovery() => array[]
        """
        raw = self.session.request('GET', 
                                   '{0}/recs/core?locale=en/'.format(self.BASE_ADDRESS),
                                   headers=self.headers)
        processed = json.loads(raw.text)
        return [Profile(user) for user in processed['results']]

    @property
    def user(self):
        """
        user() => json.object
        GETS the logged users data, retrieves a text based format, what's parsed into json format for iteration
        :return: user.json 
        """
        raw = self.session.request('GET',
                                   '{0}/v2/profile?include=user'.format(self.BASE_ADDRESS),
                                   headers=self.headers)
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
                                   '{0}/like/{1}'.format(self.BASE_ADDRESS, _id),
                                   data={'locale': 'en'},
                                   headers=self.headers)

        processed = json.loads(raw.text)

        # remove X-Padding from raw.text
        del processed['X-Padding']

        return processed

    def super_like(self, _id):
        raw = self.session.request('POST',
                                   '{0}/like/{1}/super'.format(self.BASE_ADDRESS, _id),
                                   data={'locale': 'en'},
                                   headers=self.headers)
        return json.loads(raw.text)

    def remove_super_like(self, _id):
        raw = self.session.request('DELETE',
                                   '{0}/like/{1}/super'.format(self.BASE_ADDRESS, _id),
                                   data={'locale': 'en'},
                                   headers=self.headers)
        return json.loads(raw.text)

    def dislike(self, _id):
        raw = self.session.request('GET',
                                   '{0}/pass/{1}'.format(self.BASE_ADDRESS, _id),
                                   data={'locale': 'en'},
                                   headers=self.headers)
        return json.loads(raw.text)
      
    def matches(self, count=60):
        raw = self.session.request('GET',
                                   '{0}/v2/matches?count={1}&locale=en'.format(self.BASE_ADDRESS, count),
                                   headers=self.headers)
        matches = json.loads(raw.text)['data']['matches']
        return [Match(self, match) for match in matches]

    @property
    def _id(self):
        return self.user['_id']

    @property
    def name(self):
        return self.user['name']

    @property
    def position(self):
        return self.user['pos']

    @property
    def gender(self):
        gender = self.user['gender']
        return "Female" if gender is 1 else "male"

    @property
    def age_filter_min(self):
        return self.user['age_filter_min']

    @property
    def age_filter_max(self):
        return self.user['age_filter_max']

    @property
    def birthday(self):
        return self.user['birth_date']

    @property
    def interests(self):
        raw = self.user['interests']
        return [interest for interest in raw]

    @property
    def photos(self):
        photos = self.user['photos']
        return [photo for photo in photos]

    @property
    def jobs(self):
        jobs = self.user['jobs']
        return [job for job in jobs]

    @property
    def schools(self):
        schools = self.user['schools']
        return [school for school in schools]
   
    @property
    def discoverable(self):
        return self.user['discoverable']

