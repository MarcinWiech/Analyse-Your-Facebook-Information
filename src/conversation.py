# -*- coding: utf-8 -*-
import json
import sys
from datetime import datetime
import operator
from itertools import islice
from functools import reduce

global data

class Conversation():
    def __init__(self,file_path):
        json_data = load_file(file_path)
        self.participant_names = get_names(json_data)
        self.messages = get_messages(json_data)
        self.msgs_num = len(self.messages)
        self.messages_for_participant = get_messages_for_participant(self.messages, self.participant_names)

    def get_number_of_messages_per_participant(self):
        messages_for_participant_temp = self.messages_for_participant.copy()
        for participant in messages_for_participant_temp.keys():
            messages_for_participant_temp[participant] = len(messages_for_participant_temp[participant])
        return messages_for_participant_temp
    
    def get_number_of_chars_per_participant(self):
        messages_for_participant_temp = self.messages_for_participant.copy()
        for participant in messages_for_participant_temp.keys():
            messages_for_participant_temp[participant] = get_number_of_chars(messages_for_participant_temp[participant])
        return messages_for_participant_temp

    def get_owners_contribution(self):
        try:
            owner = self.participant_names[1]
            self.messages_for_participant[owner]
        except:
            return 0
        
        owners_chars = get_number_of_chars(self.messages_for_participant[owner])
        owners_msgs = len(self.messages_for_participant[owner])
        rest_chars = 0
        rest_msgs = 0
        for participant_name in self.messages_for_participant:
            if participant_name != owner:
                rest_chars += get_number_of_chars(self.messages_for_participant[participant_name])
                rest_msgs += len(self.messages_for_participant[participant_name])
        contribution = (((owners_chars/(owners_chars+rest_chars)) + (owners_msgs/(owners_msgs+rest_msgs)))/2)*100
        return "{0:.0f}".format(contribution) +"%"

def get_number_of_chars(messages):
    counter = 0
    for message in messages:
        counter += len(message)
    return counter

def get_messages_for_participant(messages, participant_names):
    messages_for_participant = {}
    for message in messages:
        if message['sender_name'] in messages_for_participant:
            messages_for_participant[message['sender_name']].append(message)
        else:
            messages_for_participant[message['sender_name']] = [message]
    return messages_for_participant

def get_messages(json_data):
    return json_data['messages']

def get_names(json_data):
    names = []
    for p in json_data['participants']:
        names.append(p['name'])
    return names

def timestamp_to_date(timestamp):
    return datetime.fromtimestamp(timestamp/1000).date()

def load_file(file):
    global data
    with open(file) as json_file:  
        data = parse_obj(json.load(json_file))
    return data

# Parses json object and encodes properly
def parse_obj(obj):
    for category in obj:
        if isinstance(obj[category], list):
            for category_children in obj[category]:
                if isinstance(category_children, dict) :
                    for value in category_children.keys():
                        if isinstance(category_children[value], str):
                            category_children[value] = category_children[value].encode('latin_1').decode('utf-8')
    return obj