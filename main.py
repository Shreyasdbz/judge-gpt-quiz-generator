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
from typing import List
from classes.article import Article
from utils.locales import supported_locales
from generation.article_generation import generate_single_article



def main():
    """ main """
    
    generated_articles_file_path = "data/generated_articles.json"
    
    fetched_articles = []
    current_headlines:List[str] = []
    articles_to_add:List[Article] = []
    
    # Read in previously generated headlines
    with open (generated_articles_file_path, 'r') as read_file:
        data = json.load(read_file)
        fetched_articles = data["articles"]
        print(f"Retrieved {len(fetched_articles)} articles from file.")
        if(len(fetched_articles) > 0):
            for i in range(len(fetched_articles)):
                current_headlines.append(fetched_articles[i]["title"])
        read_file.close()
        
    # Generate a single article
    new_article = generate_single_article(
        locale_choices=supported_locales,
        make_fake_choices=[True, False],
        content_model_choices=["GPT-4o"],
        used_prompts_list=current_headlines
    )
    articles_to_add.append(new_article)
    
    # Write out to file
    with open(generated_articles_file_path, 'w') as write_file:
        for article in articles_to_add:
            fetched_articles.append(article.to_dict())
        json.dump({"articles": fetched_articles}, write_file, indent=4)
    

if __name__ == "__main__":
    main()
