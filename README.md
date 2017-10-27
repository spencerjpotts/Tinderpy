# Tinderpy

Who needs Tinder Select! When you have Tinderpy.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


# Discord
 [Join the Discord](https://discord.gg/262RFta)

 
### Prerequisites


```
Python~2.7
    @requests
```
## x-auth-token
Must obtain your valid x_auth_token, if you're not sure how to obtain the token please read below for further information about obtaining x-auth-token.
 

 
 To obtain your x_auth_token visit your preferred browser (I'm using chrome in the image below) > Open Web developer tools by clicking F12 or Settings > More tools > Developer Tools.
 Once open, you can now navigate to the Network tab. 
 When in the Network tab locate the left box and find the request that looks like this profile?include=user click to access its content. 
 Next to it will be some drop down lists of the headers now find the Request header and look for 'x-auth-token' the corresponding value in the x-auth-token key is your user token what you will need for Tinderpy to function.
 Looks something like the below image.
 ![x-auth-token process](https://lh4.googleusercontent.com/2HnJNud5jqqUFhwLmqgRs_JYTWZ9utTXQ2XY2LiI3y8YXhTEwgcYiG-RL8oxLrQZ0u3AhswwyAwQbkw=w1920-h974-rw)
 
    PLEASE TREAT THE X_AUTH_TOKEN AS YOU WOULD LIKE A PASSWORD

### Installing



## Running the test bot
### Example test code of Tinderpy auto liking users once every second

Open test.py using your favorite text editor, use previously obtained x-auth-token and replace it as the parameter in the User() class

```python
user = User('X-AUTH-TOKEN HERE')
```
Save test.py and proceed with executing the python script

    C://FOLDERLOCATION/ python test.py
    
# Documentation
## Refer to wiki
[Tinderpy Wiki]()
    
## Contributing
Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us.


See also the list of [contributors](https://github.com/spencerjpotts/Tinderpy/contributors) who participated in this project.

## Acknowledgments

* Hat tip to anyone who's code was used

 
# Bugs / Issues
If you find a bug in the bot, please search our issue tracker first. If it has not been reported, please create a new issue so that our team can assist you as quickly as possible.


# Disclaimer
Tinderpy is intended for academic purposes and should not be used as it violates the TOS and is unfair to the community. Use the bot at your own risk.
