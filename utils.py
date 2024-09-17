import random
import string
import json

def generate_unique_id():
    """
    Generate a unique 12-character ID.
    Returns:
        str: Unique ID
    """
    characters = string.ascii_letters + string.digits  # a-z, A-Z, 0-9
    unique_id = ''.join(random.choices(characters, k=12))
    return unique_id


def add_unique_ids_to_headlines():
    """
    Add unique IDs to the already generated headlines in json file
    Args:
    Returns:
    """

    file_path = "generated_headlines.json"
    article_objects = []
    
    with open(file_path, 'r') as read_file:
        data = json.load(read_file)
        headlines = data["headlines"]
        for article in headlines:
            article["uid"] = generate_unique_id()
            article_objects.append(article)
        read_file.close()
    
    with open(file_path, 'w') as write_file:
        json.dump({"headlines": article_objects}, write_file)
        write_file.close()
        print(
            f"""{len(article_objects)} headlines updated with unique IDs and stored in file."""
            )