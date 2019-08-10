import sys

from src.file_crawler import get_all_conversations
from src.conversation import Conversation
from src.conversation_util import get_table_one_objects
from src.generate_pdf import Document

def main(face_dir_path, save_doc_path):

    # if(len(sys.argv) != 2):
    #     print('Wrong number of arguments')
    #     return
    
    # conversations = get_all_conversations(sys.argv[1] + "/messages/inbox/")
    conversations = get_all_conversations(face_dir_path + "/messages/inbox/")
    table_objects = get_table_one_objects(conversations)
    
    document = Document()
    document.render_document(save_doc_path ,"Name", table_objects)
    
    print("FINISHED")

# if __name__ == "__main__":
#     main()