'''
# file: message_match_example.py
# Author: 
# Date: 3/18/2019
# Description: 
    Example of Tinderpy auto messaging 

'''

# imoort the tinderpy.py module to have access to the api.
import tinderpy

# assign the variable 'user' to the class Object 'User'
user = tinderpy.User('X-AUTH-TOKEN')

# prompt user welcome message and also include the logged users name using the users object 'user'.name()
print("[!] Welcome ", user.name)

# obtain all matches for the current logged account.
matches = user.matches()
for match in matches:
    if len(match.messages) is 0:
        match.message("Hello.")