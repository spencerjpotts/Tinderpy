'''

    Example of Tinderpy auto liking users once every second
'''

import time
from tinderpy import User


user = User('X-AUTH-TOKEN')

print("[!] Welcome %s" % user.name())

# collect list of newly added nearby matches and put them in matches var
matches = user.subjects()  # user.subjects() returns array of match objects

# Iterate over each individual user in matches[] and pass their id into the like def
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
