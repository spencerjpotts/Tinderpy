
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

    def __init__(self, token):
        self.session = requests.session()
        self.x_auth_token = token

    def discovery(self):
        """
        discovery() => array[]
        """
        raw = self.session.request('GET', 
                                   'https://api.gotinder.com/recs/core?locale=en/',
                                   headers={'x-auth-token': self.x_auth_token})
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

        processed = json.loads(raw.text)

        # remove X-Padding from raw.text
        del processed['X-Padding']

        return processed

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
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/pass/%s' % _id,
                                   data={'locale': 'en'},
                                   headers={'x-auth-token': self.x_auth_token})
        return json.loads(raw.text)
      
    def matches(self, count=60):
        raw = self.session.request('GET',
                                   'https://api.gotinder.com/v2/matches?count={0}&locale=en'.format(count),
                                   headers={'x-auth-token': self.x_auth_token})
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
    def gender(self):  # gets the gender M/F
        gender = self.user['gender']
        # if gender is 0:  # Male
        #     return "Male"
        # elif gender is 1:  # Female
        #     return "Female"
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
        # arr = []
        # for photo in photos:
        #     arr.append(photo)
        return [photo for photo in photos]

    def jobs(self):
        jobs = self.user['jobs']
        # arr = []
        # for job in jobs:
        #     arr.append(job)
        # return arr
        return [job for job in jobs]

    def schools(self):
        schools = self.user['schools']
        # arr = []
        # for school in schools:
        #     arr.append(school)
        # return arr
        return [school for school in schools]
   
    def discoverable(self):
        return self.user['discoverable']

