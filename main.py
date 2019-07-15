import sys

from file_crawler import get_all_conversations
from conversation import Conversation
from conversation_util import *
from pdf_test import Document

def main():
    if(len(sys.argv) != 2):
        print('Wrong number of arguments')
        return
    conversations = get_all_conversations(sys.argv[1]+"/messages/inbox/")
    document = Document()
    table_objects = get_table_one_objects(conversations)
    document.render_document("Marcin",table_objects)   
    
    print("FINISHED")

if __name__ == "__main__":
    main()