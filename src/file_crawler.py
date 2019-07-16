import os, fnmatch, operator
from collections import OrderedDict
from src.conversation import Conversation
from src.conversation_util import get_message_number_per_conversation 

def get_all_conversations(root_dir_path):
    filepaths = find("message_1.json", root_dir_path)
    return get_all_conversations_from_filepaths(filepaths)

def get_all_conversations_from_filepaths(filepaths):
    conversations = []
    for filepath in filepaths:
        conversations.append(get_conversation_from_file(filepath))
    return conversations

def get_conversation_from_file(filepath):
    return Conversation(filepath)

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

#/home/marcin/Projects/Facebook_analysis
def main():
    files = find("message_1.json", '/home/marcin/Projects/Facebook_analysis/messages/inbox/')     
    print(len(files))
    conversation = get_conversation_from_file(files[0])
    print(conversation.participant_names)
    conversations = get_all_conversations_from_filepaths(files)
    print(len(conversations))
    conv_num = list(get_message_number_per_conversation(conversations))
    for i in range(30):
        print(i+1,':',conv_num[i])

if __name__ == "__main__":
    main()