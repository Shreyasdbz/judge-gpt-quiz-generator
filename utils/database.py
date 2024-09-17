import os
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



def store_articles_to_db(mode:str, articles: List[Article]) -> bool:
    """
    ### Store articles in the database.
    #### Args:
    - mode (str): The mode to run the database in (dev, prod, testing).
    - articles (List[Article]): List of articles to store in the database.
    #### Returns:
    - bool: True if successful, False otherwise.
    """
    print(
    f'''
    Starting to store {len(articles)} articles in the database.
    '''
    )
    
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
    
    return True