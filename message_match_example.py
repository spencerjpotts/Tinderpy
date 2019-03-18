'''
# file: message_match_example.py
# Author: 
# Date: 3/18/2019
# Description: 
    Example of Tinderpy auto messaging 

'''

# imoort the tinderpy.py module to have access to the api.
import tinderpy

# assign the variable 'user' to the class Object User
user = tinderpy.User('X-AUTH-TOKEN')

# prompt user welcome message and also include the logged users name using the users object 'user'.name()
print("[!] Welcome ", user.name())

# obtain all matches for the current logged account.
matches = user.matches()

# loop over each individual match in the matches object and call the message() function.;
for match in matches:
    if len(match.messages) < 0:
        # assign the response of match.message(String)
        # message(String) will return a http json repsonse;
        response = match.message("Hello.")

        # display json response to console screen
        print(response)
    else:
        # if user already has existing converstion with logged user then promt message.
        print(match.name, "Already has a converstion started.")