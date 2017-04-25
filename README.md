# SocialMediaManager
Social Media management tool.
  - allow you to post on all you social media at once.

# Media supoprted :
Currently supports :
  - Facebook (post only)
  - Twitter (post only)

Planning :
  - Google+
  - WikiCrans (wiki.crans.rog)
  - Adding tutorials to get tokens on a wiki page

# Dépendancies :
 * facebook-sdk :  
  ```sh 
    pip3 install -e git+https://github.com/mobolic/facebook-sdk.git#egg=facebook-sdk
  ```
 * python-twitter : 
  ```sh
    pip3 install twitter-sdk
  ```

# Help :
  ```sh
    usage: socialmediamanager.py [-h] [-f] [-t] [-g] message_to_post
    
    Script perrmettant de poster un messge sur les réseaux sociaux spécifiés
    
    positional arguments:
       message_to_post  poste le message sur les réseaux sélectionnés

    optional arguments:
       -h, --help       show this help message and exit
       -f, --facebook   poste sur facebook
       -t, --twitter    poste sur twitter
       -g, --google     poste sur google+
  ```

# Credentials : 
You need to fill the credential.py with some login informations (you get them from your apps on social media) :
   - Tutorial here for twitter :  http://python-twitter.readthedocs.io/en/latest/getting_started.html
   - Here for facebook : http://stackoverflow.com/questions/17197970/facebook-permanent-page-access-token



