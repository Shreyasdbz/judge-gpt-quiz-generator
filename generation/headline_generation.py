'''
This is the headline generation module. It generates news headlines using the GPT-4o Mini model.
'''

import os
import json
import random
import openai
from models.article import news_outlets_map
from utils.utils import generate_unique_id


openai.api_key = os.getenv("JUDGE_GPT_OPENAI_API_KEY")
# Throw error if API key is not set
if openai.api_key is None:
    raise ValueError(
        '''
        [headline_generation] API key is not set. 
        Please set the OPENAI_API_KEY environment variable.
        '''
        )

def generate_single_headline(news_outlet, locale, make_fake, used_prompts_list = []):
    """ 
    Generate a news headline using the GPT-4o Mini model.
    Args:
        news_outlet (str): The news outlet to emulate
        locale (str): The locale to write the headline in
        make_fake (bool): Flag indicating if the headline should be fake
        used_prompts_list (list): List of prompts to avoid repeating
    Returns:
        Tuple: Headline and context
    """

    print(
    f'''
    Generating headline with GPT-4o Mini model.
    For `{news_outlet}` in `{locale}` language. Is fake: `{make_fake}`
    '''
    )
    additional_prompt = ""
    if make_fake:
        additional_prompt = "Write a fake news article headline. The headline should sound at least fairly realistic."
    else:
        additional_prompt = "Write a real news article headline."            

    topicss_to_use = [
        "recent events",
        "international politics",
        "international sports",
        "science",
        "technology",
        "planet",
        "health",
        "nature",
        "space",
        "economy",
        "business",
        "international entertainment",
        "international culture",
        "international art",
        "international music",
        "international cinema",
        "international literature",
        "international fashion",
        "international food",
        "international travel",
        "international lifestyle",
        "international environment",
        "international climate",
        "international energy",
        "international education",
        "international society",
        "international history",
    ]
    
    topics_to_avoid = [
        "local",
        "regional",
        "religion",
        "not safe for work",
        "adult content",
    ]
    
    
  
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # Primary prompt
            {"role": "system", "content": 
                '''
                    You are a journalist writing a news article's headline.
                    Just the headline + some context used to generate it is needed.
                    The headline should be 8-14 words long.
                    Don't include double quotes in the headline.
                    Write the headline one 1 line and the context on the next line.
                    Don't include the headline in the context.
                    Don't say "headline" or "context" in the response.
                    Avoid leaving trailing white spaces.
                    Make the context 2-3 sentences long.
                    Add some nuanced details to the context.
                    Make the topics relevant to the news outlet provided.
                    Pick topics that are usually attention-grabbing and try to avoid mundane ones.
                '''
            },
            # Topics to use
            {"role": "system", "content": f"Topics to use: {topicss_to_use}"},
            # Topics to avoid
            {"role": "system", "content": f"Topics to avoid: {topics_to_avoid}"},
            # Fake or real news conditional prompt
            {"role": "system", "content": additional_prompt},
            # News outlet to emulate
            {"role": "system", "content": f"Emulate the style of the news outlet: {news_outlet}."},
            # Locale to write in
            {"role": "system", "content": f"Write the article in {locale} language. Add in some nuanced details."},
            # Avoid repeating prompts
            {"role": "system", "content": f"Don't repeat from these prompts: {used_prompts_list}"},
        ]
    )
    
    content = response.choices[0].message.content
    # Extract the headline from the response
    headline = content.split("\n")[0]
    # Extract the context from the response
    context = content.split("\n")[1]

    # Tuple of headline and context
    return headline, context


def generate_multiple_headlines(generate_limit, make_fake_choices, locales_to_use, generated_headlines_file_path):
    """
    Generate multiple news headlines using the GPT-4o Mini model.
    Args:
        generate_limit (num): Limit of headlines to generate
        make_fake_choices (list<bool>): Type of headlines to generate [True, False]
        locales_to_use (list): List of locales to generate headlines for
        generated_headlines_file_path (str): Path to the file to store / retrieve the generated headlines
    """

    fetched_headline_objects = []
    current_headlines = []
    
    # Open json file to retrieve generated headlines
    with open (generated_headlines_file_path, 'r') as read_file:
        data = json.load(read_file)
        fetched_headline_objects = data["headlines"]
        print(f"Retrieved {len(fetched_headline_objects)} headlines from file.")
        for headline in fetched_headline_objects:
            current_headlines.append(headline["title"])
        read_file.close()
    
    # Loop through the generate_limit
    for i in range(generate_limit):

        # Params for each headline
        locale_to_use = random.choice(locales_to_use)
        style_to_use = random.choice(news_outlets_map[locale_to_use])
        make_fake = random.choice(make_fake_choices)

        # Generate a headline
        headline_text, context_text = generate_single_headline(
            news_outlet=style_to_use,
            locale=locale_to_use,
            make_fake=make_fake,
            used_prompts_list=current_headlines
        )
        current_headlines.append(headline_text)
        fetched_headline_objects.append({
            "uid": generate_unique_id(),
            "title": headline_text,
            "origin_locale": locale_to_use,
            "style": style_to_use,
            "is_fake": make_fake,
            "headline_generation_model_used": "GPT-4o Mini",
            "headline_context": context_text,
        })
    
    # Write the generated headlines to the json file
    with open(generated_headlines_file_path, 'w') as write_file:
        json.dump({"headlines": fetched_headline_objects}, write_file)
        write_file.close()
        print(
            f"""{generate_limit} headlines generated and stored in file."""
            )
        


     
    