# String helper

import uuid

def generate_uuid(length):
    
    id = str(uuid.uuid1())

    return id[0:length]