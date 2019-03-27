'''
    @file: test.py
    @author: Spencerjpotts
    @date: 3/24/2019
    @description:  
        Example of Tinderpy auto liking users once every 3 second.
    @usage: 
        python test.py

    @caution-warning
     beaware of leaving text script running for long periods of time. 
     MAY CAUSE ACCOUNT PUNISHMENT.
'''

import time
import tinderpy

#
user = tinderpy.User('X-AUTH-TOKEN')

# Prompt a welcome message for the logged user.
print("[!] Welcome %s" % user.name)


# loop will run forever
# force stop script to exit loop.
while True:

    # user.discovery() returns array of 'Match' class types.
    discovery = user.discovery()

    # Loop over each person/profile class/object in the discovery array.
    for person in discovery:

        # liking a profile is simple. Just call the user.like() method
        # and pass each array class elemnt 'Profile'
        like_response = user.like(person)
        
        # Log some Profile/persons information to the console. 
        print("ID: {0}\nName: {0.name}\nBio: {0.bio}".format(person))

        # print 'like' http request response to the console.
        print(like_response)

        # cause flow of script to sleep for 3seconds to help http request loading and not get flooded
        # with requests and cause suspicious activity.
        time.sleep(3)
