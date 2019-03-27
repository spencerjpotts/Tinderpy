
"""
    @Author: Spencer J Potts
    @Description: Automates tinder functionality.
    @Date: 

"""

from .message import MessageTemplate

class Match(object):
    def __init__(self, parent, match):
        self.parent = parent
        self.session = parent.session

        self.matchObject = match
    
    @property
    def id(self):
        return self.matchObject['id']

    @property
    def _id(self):
        return self.matchObject['person']['_id']

    @property
    def name(self):
        return self.matchObject['person']['name']

    @property
    def gender(self):
        return self.matchObject['person']['gender']

    @property
    def messages(self):
        raw = self.session.request('GET', 
                                   'https://api.gotinder.com/v2/matches/{0}/messages?count=100&locale=en'.format(self.id), 
                                   headers={'x-auth-token': self.parent.x_auth_token})
        
        return [MessageTemplate(data) for data in raw.json()['data']['messages']][::-1]

    def message(self, msg):
        data = {
            "matchId": self.id,
            "message": msg,
            "userId": self.parent._id()
        }
        raw = self.session.request('POST',
                                    'https://api.gotinder.com/user/matches/{0}?locale=en'.format(self.id),
                                    headers={'x-auth-token': self.parent.x_auth_token},
                                    data=data)
        return raw.json()

    def remove(self):
        raw = self.session.request('DELETE',
                                   'https://api.gotinder.com/user/matches/{0}?locale=en'.format(self.id),
                                    headers={'x-auth-token': self.parent.x_auth_token})
        return raw.json()

    def __str__(self):
        return self.id