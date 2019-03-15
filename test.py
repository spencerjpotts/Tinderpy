'''

    Example of Tinderpy auto liking users once every second
'''

import time
import tinderpy


user = tinderpy.User('X-AUTH-TOKEN')

print("[!] Welcome %s" % user.name())

while True:
    matches = user.discovery()  # user.subjects() returns array of match objects
    for match in matches:
        # Like user with ID
        user.like(match['_id'])

        # Print name of the user just liked and print a message ''EMPTY BIO'' if the persons bio was empty
        print("""
           -----------------------------
           Name: %s
           Bio: %s
           -----------------------------
           """ % (match['name'], match['bio'] if len(match['bio']) > 0 else "EMPTY BIO"))

        # Sleep for one second
        time.sleep(1)