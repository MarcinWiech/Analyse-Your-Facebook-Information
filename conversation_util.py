# Ignores groups

class Table_One_Object():
    def __init__(self,participant_name, number_of_mssgs, owners_contribution):
        self.participant_name = participant_name
        self.number_of_mssgs = number_of_mssgs
        self.owners_contribution = owners_contribution

def get_table_one_objects(conversations):
    objects = []
    sort_conversations_by_message_number(conversations)
    for conversation in conversations:
        
        names = conversation.participant_names
        if len(names) == 2:
            name = names[0]
            number_of_msgs = conversation.msgs_num
            owners_contribution = conversation.get_owners_contribution()
            objects.append(Table_One_Object(name,number_of_msgs,owners_contribution))
    return objects

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

def sort_conversations_by_message_number(conversations):
    return conversations.sort(key=lambda x : len(x.messages), reverse = True)