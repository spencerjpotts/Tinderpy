"""
    @Author: Spencer J Potts
    @Description: Automates tinder functionality.
    @Date:  

"""

class Profile:
    """
    docstring
    """
    def __init__(self, data):
        self.data = data
    
    @property
    def id(self):
        return self.data['_id']

    @property
    def name(self):
        return self.data['name']

    @property
    def bio(self):
        return self.data['bio']
    
    @property
    def birthdate(self):
        return self.data['birth_date']

    @property
    def jobs(self):
        return self.data['jobs']

    @property
    def schools(self):
        return self.data['schools']

    @property
    def gender(self):
        return "female" if self.data['gender'] is 1 else "male"

    @property
    def distance(self):
        return self.data['distance_mi']

    def __str__(self):
        return self.id