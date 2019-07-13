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
        self.messages_for_participant = get_messages_for_participant(self.messages, self.participant_names)

    def get_number_of_messages_per_participant(self):
        messages_for_participant_temp = self.messages_for_participant.copy()
        for participant in messages_for_participant_temp.keys():
            messages_for_participant_temp[participant] = len(messages_for_participant_temp[participant])
        return messages_for_participant_temp
    
    def get_number_of_chars_per_participant(self):
        messages_for_participant_temp = self.messages_for_participant.copy()
        for participant in messages_for_participant_temp.keys():
           # print('DEBUG', messages_for_participant_temp)
            messages_for_participant_temp[participant] = get_number_of_chars(messages_for_participant_temp[participant])
        return messages_for_participant_temp

    

def main():
    if(len(sys.argv) != 2):
        print('Wrong number of arguments')
        return

   
    # json_data = load_file(sys.argv[1])
    # messages_per_participant(json_data)
    # messages_per_day(json_data)
    # busies_days(json_data)
    conversation = Conversation(sys.argv[1])
    
    for key in conversation.messages_for_participant.keys():
        print(key, len(conversation.messages_for_participant[key]))
        print(key, get_number_of_chars(conversation.messages_for_participant[key]))
    
    print(conversation.get_number_of_chars_per_participant())

    
   

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

#(participant, messages[])


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

# DEPRECATED --------------------------------------------------------------------------------------------------------------------------------
def messages_per_participant(json_data):
    names = get_names(json_data)
    print('--- number of messages ---')
    for i in range(len(names)):
          print(names[i] + ": " + str(count_messages(names[i], 'sender_name', json_data)))
    print('--- number of characters ---')
    for i in range(len(names)):
          print(names[i] + ": " + str(number_of_messages_chars(names[i], json_data)))
    print('--- number of stickers ---')
    for i in range(len(names)):
          print(names[i] + ": " + str(count_messages(names[i], 'sticker', json_data)))
    print('--- number of photos ---')
    for i in range(len(names)):
          print(names[i] + ": " + str(count_messages(names[i], 'photos', json_data)))

def busies_days(json_data):
    messages = messages_per_day(json_data)
    size = 10 if len(messages) > 9 else len(messages)
    for i in range(size):
        print(messages[i][0], ":", messages[i][1])

def messages_per_day(json_data):
    date_msgs =	{}
    for message in json_data['messages']:
        date = timestamp_to_date(message['timestamp_ms'])
        if date_msgs.__contains__(date):
            date_msgs[date] += 1
        else:
            date_msgs[date] = 1
                
    return sorted(date_msgs.items(), key=lambda x: x[1], reverse = True)

def number_of_messages_chars(name, json_data):
    counter = 0
    for message in json_data['messages']:
        if message['sender_name'] == name:
            if(message.get('content')):
                counter += len(message.get('content'))
    return counter

#type is sender_name, sticker, photos
def count_messages(name, type, json_data):
    counter = 0
    for m in json_data['messages']:
        if m['sender_name'] == name:
            if(m.get(type)):
                counter += 1
    return counter

if __name__ == '__main__':
    main()