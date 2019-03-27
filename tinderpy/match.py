
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
                                   '{0}/v2/matches/{1}/messages?count=100&locale=en'.format(self.parent.BASE_ADDRESS, self.id), 
                                   headers=self.parent.headers)
        
        return [MessageTemplate(data) for data in raw.json()['data']['messages']][::-1]

    def message(self, msg):
        data = {
            "matchId": self.id,
            "message": msg,
            "userId": self.parent._id()
        }
        raw = self.session.request('POST',
                                    '{0}/user/matches/{1}?locale=en'.format(self.parent.BASE_ADDRESS, self.id),
                                    headers=self.parent.headers,
                                    data=data)
        return raw.json()

    def remove(self):
        raw = self.session.request('DELETE',
                                   '{0}/user/matches/{1}?locale=en'.format(self.parent.BASE_ADDRESS, self.id),
                                    headers=self.parent.headers)
        return raw.json()

    def __str__(self):
        return self.id