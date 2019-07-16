import sys

from src.file_crawler import get_all_conversations
from src.conversation import Conversation
from src.conversation_util import get_table_one_objects
from src.generate_pdf import Document

def main():

    if(len(sys.argv) != 2):
        print('Wrong number of arguments')
        return
    
    conversations = get_all_conversations(sys.argv[1]+"/messages/inbox/")
    table_objects = get_table_one_objects(conversations)
    
    document = Document()
    document.render_document("Marcin",table_objects)   
    
    print("FINISHED")

if __name__ == "__main__":
    main()