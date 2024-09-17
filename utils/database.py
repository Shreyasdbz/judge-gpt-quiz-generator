import os
import json
from typing import List
from pymongo import MongoClient
from classes.article import Article

# ------------------------------
# Set up
# ------------------------------
mongo_db_connection_string = os.getenv("JUDGE_GPT_MONGODB_CONNECTION_STRING")
if mongo_db_connection_string is None:
    raise ValueError(
    '''
    [database] MongoDB connection string is not set. 
    Please set the JUDGE_GPT_MONGODB_CONNECTION_STRING environment variable.
    '''
    )

database_name_dev = "dev"
database_name_prod = "prod"
database_name_testing = "testing"
collection_name_articles = "articles"


def pull_generated_headlines_from_db(mode:str, storage_file_path: str) -> List[str]:
    """
    ### Pull generated headlines from the database and store them in a file if they are not already present.
    - Headlines are pulled in 'en' (English) locale only.
    #### Args:
    - mode (str): The mode to run the database in (dev, prod, testing).
    - storage_file_path (str): The path to store the pulled headlines.
    #### Returns:
    - List[str]: List of headlines pulled from the database.
    """
    
    print(f"Pulling headlines from the database in `{mode}` mode.")
    
    # Fetch currently stored headlines
    current_headlines = []
    with open(storage_file_path, "r") as file:
        data = json.load(file)
        current_headlines = data["headlines"]
        print(f"Retrieved {len(current_headlines)} headlines from file.")
        file.close()
    
    client = MongoClient(mongo_db_connection_string)
    database_name = ""
    if(mode == "dev"):
        database_name = database_name_dev
    elif(mode == "prod"):
        database_name = database_name_prod
    elif(mode == "testing"):
        database_name = database_name_testing
        
    db = client[database_name]
    collection = db[collection_name_articles]
    
    # Pull headlines from the database
    headlines = collection.find({}, {"localized_headline_en": 1, "_id": 0})
    for headline in headlines:
        current_headlines.append(headline["localized_headline_en"])
    
    # Store the headlines in the file
    with open(storage_file_path, "w") as file:
        json.dump({"headlines": current_headlines}, file)
        file.close()

    print(f"Stored {len(current_headlines)} headlines in the file.")


def store_articles_to_db(mode:str, articles: List[Article]) -> bool:
    """
    ### Store articles in the database.
    #### Args:
    - mode (str): The mode to run the database in (dev, prod, testing).
    - articles (List[Article]): List of articles to store in the database.
    #### Returns:
    - bool: True if successful, False otherwise.
    """
    print("Starting to store {len(articles)} articles in the database.")
    
    client = MongoClient(mongo_db_connection_string)
    database_name = ""
    if(mode == "dev"):
        database_name = database_name_dev
    elif(mode == "prod"):
        database_name = database_name_prod
    elif(mode == "testing"):
        database_name = database_name_testing

    db = client[database_name]
    collection = db[collection_name_articles]    
    
    collection.insert_many(articles)
        
    client.close()
    
    print(f"""
    -----------------------------------
    ->>> Database storage
    - Successfully stored {len(articles)} articles in the database.
    -----------------------------------
    """
    )
    
    return True