#!/usr/bin/env python3

#Permet de poster sur facebook.
#Required : facebook-sdk


import facebook
import argparse
import credentials

def post_facebook(message_to_post):
	''' Poste le message sur facebook'''
	token = credentials.facebook_token
	graph = facebook.GraphAPI(access_token=token, version='2.9')
	graph.put_object(parent_object='me', connection_name='feed', message=message_to_post)













#parseur
parser = argparse.ArgumentParser(description='Plop')
parser.add_argument('-f', '--facebook', help='poste sur facebook', action='store_true')
parser.add_argument('-t', '--twitter', help='poste sur twitter', action='store_true')
parser.add_argument('-g', '--google', help='poste sur google+', action='store_true')
parser.add_argument('message_to_post', help='poste le message sur les réseaux sélectionnés', type=str)






args = parser.parse_args()
if args.message_to_post :
	if args.facebook :
		post_facebook(args.message_to_post)
