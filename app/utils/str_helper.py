# String helper

<<<<<<< HEAD
import uuid

def generate_uuid(length):
    
    id = str(uuid.uuid1())

    return id[0:length]
=======
import secrets

def generate_uuid(length):
    return secrets.token_hex(length)
>>>>>>> ee6c30bbb9ffcfc4922c4a1ed46307d23ffecb99
