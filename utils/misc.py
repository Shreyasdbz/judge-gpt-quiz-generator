import random
import string

def generate_unique_id():
    """
    ### Generate a unique 12-character ID.
    #### Returns:
    - str: Unique ID
    """
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    unique_id = ''.join(random.choices(characters, k=12))
    return unique_id
