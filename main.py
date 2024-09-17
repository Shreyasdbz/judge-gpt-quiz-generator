'''
Project oveview:
This app generates news articles (and headlines) in various languages using different news
outlets styles via a combination of GPT-4o and various other LLMs. Each article is also
translated into all 4 supported languages.
News headline generation is handled by ChatGPT-4o and content generation is handled by the
respective LLMs. These include GPT-4, GPT-4o, Phi-3-medium-4k-instruct, Llama-2,
Meta-Llama-3.1, Mistral-large, etc.
'''

import json
from utils.database import store_articles_to_db
from generation.article_generation import generate_and_store_single_article


def main():
    """ main """
    
    run_count = 1
    
    # Generate articles
    for _ in range(run_count):
        generate_and_store_single_article()
    
    # Retrieve articles from file and store articles in database
    generated_articles_file_path = "data/generated_articles.json"
    with open (generated_articles_file_path, 'r') as read_file:
        data = json.load(read_file)
        articles = data["articles"]
        print(f"Retrieved {len(articles)} articles from file.")
        read_file.close()
    # Store in database
    db_result = store_articles_to_db("testing", articles)
    if db_result:
        print(f"Stored {len(articles)} articles in database.")
    
    # Empty the array in the file
    with open(generated_articles_file_path, 'w') as write_file:
        json.dump({"articles": []}, write_file)
        write_file.close()
    print(f"Emptied {generated_articles_file_path} file.")
    
if __name__ == "__main__":
    main()
