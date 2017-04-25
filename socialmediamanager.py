#!/usr/bin/env python3

import facebook #require facebook-sdk
import twitter #require python-twitter

import argparse
import credentials as cr

def post_facebook(message_to_post):
    ''' Post on facebook'''
    api_fb = facebook.GraphAPI(access_token=cr.facebook_token, version='2.9')
    api_fb .put_object(parent_object='me', connection_name='feed', message=message_to_post)

def post_twitter(message_to_post):
    '''Post on twitter'''
    api_tw = twitter.Api(consumer_key=cr.twitter_consumer_key,
                         consumer_secret=cr.twitter_consumer_secret,
                         access_token_key=cr.twitter_access_token,
                         access_token_secret=cr.twitter_access_token_secret)
    api_tw.PostUpdate(message_to_post)

def post_google(message_to_post):
    '''Post on google+ (WIP)'''
    print('WIP')


#parseur
parser = argparse.ArgumentParser(description='Post one message on all the specified media')
parser.add_argument('-f', '--facebook', help='post on facebook', action='store_true')
parser.add_argument('-t', '--twitter', help='post on twitter', action='store_true')
parser.add_argument('-g', '--google', help='post on google+', action='store_true')
parser.add_argument('message_to_post', help='', type=str)






args = parser.parse_args()
if args.message_to_post :
    if args.facebook :
        post_facebook(args.message_to_post)
        if args.twitter :
            try :
                post_twitter(args.message_to_post)
            except :
                print("Erreur")
