import os, fnmatch, operator
from collections import OrderedDict
from conversation import Conversation


def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def get_conversation_from_file(filepath):
    return Conversation(filepath)

def get_all_conversations(filepaths):
    conversations = []
    for filepath in filepaths:
        conversations.append(get_conversation_from_file(filepath))
    return conversations



# Ignores groups
def get_message_number_per_conversation(conversations):
    conversation_number = {}
    for conversation in conversations:
        names = conversation.participant_names
        if len(names) == 2:
            conversation_number[names[0]] = \
            (len(conversation.messages), \
            sorted(conversation.get_number_of_messages_per_participant().items(), key=lambda x : x[1], reverse=True), \
            sorted(conversation.get_number_of_chars_per_participant().items(), key=lambda x : x[1], reverse=True))
    return sorted(conversation_number.items(), key=lambda x: x[1][0], reverse=True)

#/home/marcin/Projects/Facebook_analysis
def main():
    files = find("message_1.json", '/home/marcin/Projects/Facebook_analysis/messages/inbox/')     
    print(len(files))
    conversation = get_conversation_from_file(files[0])
    print(conversation.participant_names)
    conversations = get_all_conversations(files)
    print(len(conversations))
    conv_num = list(get_message_number_per_conversation(conversations))
    for i in range(30):
        print(i+1,':',conv_num[i])

if __name__ == "__main__":
    main()