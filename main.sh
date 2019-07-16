#!/usr/bin/env python3
import sys

from src.file_crawler import get_all_conversations
from src.conversation import Conversation
from src.conversation_util import get_table_one_objects
from src.generate_pdf import Document

def main():

    conversations = get_all_conversations("../Facebook_analysis/messages/inbox/")
    table_objects = get_table_one_objects(conversations)
    
    document = Document()
    document.render_document("Marcin",table_objects)   

if __name__ == "__main__":
    main()