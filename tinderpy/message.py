
"""
    @Author: Spencer J Potts
    @Description: Automates tinder functionality.
    @Date: 5/22/2018  


    "_id": "string",
    "match_id": "string",
    "sent_date": "date/String",
    "message": "string",
    "to": "string",
    "from": "string",
    "created_date": "string",
    "timestamp": int

"""

class MessageTemplate():
    def __init__(self, data):
        self.data = data
    
    @property
    def id(self):
        return self.data['_id']
    
    @property
    def to(self):
        return self.data['to']

    @property
    def ffrom(self):
        return self.data['from']

    @property
    def message(self):
        return self.data['message']
    
    def __str__(self):
        return self.message