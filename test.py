'''

    Example of Tinderpy auto liking users once every second
'''

import time
import tinderpy



user = tinderpy.User('TOKEN HERE')

print("[!] Welcome %s" % user.name())


# loop will run for ever
while True:

    # user.discovery() returns array of match json objects
    discovery = user.discovery()

    # Loop over each person/profile class/object in the discovery array.
    for person in discovery:

        # liking a profile is simple. Just call the user.like() method
        # and pass the discovered array populated with 'Profile' classes/objects
        # A 'Profile' class/object will return its self ID.
        user.like(person)
        like_response = user.like(person)
        
        # Log some Profile/persons information to the console. 
        print("ID: {0}\nName: {1}\nBio: {2}".format(person, person.name, person.bio))

        # print 'like' http request response to the console.
        print(like_response)

        # cause flow of script to sleep for 3seconds to help http request loading not get flooded
        # and cause suspicious activity.
        time.sleep(3)