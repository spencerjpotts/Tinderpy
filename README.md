# Tinderpy

Who needs Tinder Select! When you have Tinderpy.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.


# Discord
**Join our community and start contributing and sharing!**
 
 [Join the Discord](https://discord.gg/262RFta)

 
# Prerequisites
## Python
Please ensure you have Python installed on your system.
IF you are not sure how to install Python visit [python.org](https://www.python.org/) for installation steps

```
Python~2.7
    @requests
```

### Requests package
Tinderpy uses pythons requests package, to install requests:

Open command prompt (pip is installed alongside with python) and type:
    
    $ pip install requests
   
Make sure python/pip is a part of the environment variable PATH!

For more documentation on [Python Requests Doc](http://docs.python-requests.org)
        
## x-auth-token
Must obtain your valid **_x_auth_token_**, if you're not sure how to obtain the token please read below for further information about obtaining x-auth-token.
 

 
 To obtain your **x_auth_token** Visit your preferred browser (I'm using chrome in the image below) continue to login at [Tinder.com](https://tinder.com) 
 
 (You may need to refresh the page for developer console to recapture http events) 
 
 **_Open Web developer_** with **_F12_** or **_Settings_** **>** **_More tools_** **>** **_Developer Tools._**
 
 Once open, you can now navigate to the **_Network tab_**. 
 When in the Network tab locate the left box and find the request that looks like this **_/profile?include=user_** or scroll down and click links until you find **_x-auth-token_** and click to access its content.
  
 Next to it will be some drop down lists of the headers now find the Request header and look for '**_x-auth-token_**' the corresponding value in the x-auth-token key is your user token what you will need for **_Tinderpy_** to function.
 
 Looks something like the below image.
 ![x-auth-token process](https://i.imgur.com/IEgUeDv.png)
 
    PLEASE TREAT THE X_AUTH_TOKEN AS YOU WOULD LIKE A PASSWORD


## Running the test bot
### Example Test code of Tinderpy Auto liking users once every second
Once you have downloaded a copy of Tinderpy, navigate to the downloaded directory.
Open test.py using your favorite text editor and use previously obtained x-auth-token as the parameter in the User() class

```python
user = User('X-AUTH-TOKEN HERE') 
```
Save test.py and proceed with executing the python script like so:

Open command prompt (CMD) and navigate to the Tinderpy directory using
This will place you inside Tinderpys directory

    c:\WHERE\YOU\DOWNLOADED> cd Tinderpy
    
Once inside run this command to start the Tinderpy test.py script

    c:\WHERE\YOU\DOWNLOADED\Tinderpy> python test.py
    
# Documentation
## Quick Reference
```python

```
## Refer to wiki
[Tinderpy Wiki]()
    
## Contributing
Please read [CONTRIBUTING.md]() for details on our code of conduct, and the process for submitting pull requests to us.


See also the list of [contributors](https://github.com/spencerjpotts/Tinderpy/contributors) who participated in this project.

## Acknowledgments

* Hat tip to anyone who's code was used

 
# Bugs / Issues
If you find a bug in the bot, please search our issue tracker first. If it has not been reported, please create a new issue so that our team 'I' can assist you as quickly as possible.


# Disclaimer
**_Tinderpy_** is intended for academic purposes and should not be used as it violates the TOS and is unfair to the community. 

**_Use the bot at your own risk._**

# Donate
[![](https://www.paypalobjects.com/en_AU/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=NUM5LS6HQ5CCQ&currency_code=AUD&source=url)