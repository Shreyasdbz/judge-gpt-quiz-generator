'''
Project oveview:
This app generates news articles (and headlines) in various languages using different news
outlets styles via a combination of various other LLMs. Each article is also
translated into all 4 supported languages.
News headline generation is handled by specified model and content generation is handled by the
respective LLMs. These include GPT-4, GPT-4o, Phi-3-medium-4k-instruct, Llama-2,
Meta-Llama-3.1, Mistral-large, etc.
'''

import json
from utils.database import store_articles_to_db
from generation import article_generation


def generate_and_push_to_db(db_name, model):
    run_count = 1
    
    # Generate articles
    for i in range(run_count):
        print(f"""
        ================================================================================
        ->>> Generating Article {i+1} of {run_count} now...
        ================================================================================
        """
        )
        article_generation.generate_and_store_single_article(model)
    
    # Retrieve articles from file and store articles in database
    article_generation.ARTICLES_FILE_PATH
    with open (article_generation.ARTICLES_FILE_PATH, 'r') as read_file:
        data = json.load(read_file)
        articles = data["articles"]
        print(f"Retrieved {len(articles)} articles from file.")
        read_file.close()

    # Store in database
    db_result = store_articles_to_db(db_name, articles)
    if db_result:
        print(f"Stored {len(articles)} articles in database.")
    
    # Empty the array in the file
    with open(article_generation.ARTICLES_FILE_PATH, 'w') as write_file:
        json.dump({"articles": []}, write_file)
        write_file.close()
    
    print(f"Emptied {article_generation.ARTICLES_FILE_PATH} file.")    



def main():
    """ main """
    
    print(
    """
    ================================================================================
    ->>> Welcome to the News Article Generation App!
    - Add in a function call below to get started.
    ================================================================================
    """
    )  
    
    # generate_and_push_to_db(db_name="dev")

    model_list = [
        "Phi-3.5-mini-instruct",
    ]

    for model in model_list:
        generate_and_push_to_db(db_name="testing", model=model)

    
if __name__ == "__main__":
    print("Starting...")
    main()
