'''
This is the headline generation module. It generates news headlines using the GPT-4o Mini model.
'''

import os
import openai
from utils.locales import locale_codes_to_names_map


openai.api_key = os.getenv("JUDGE_GPT_OPENAI_API_KEY")
# Throw error if API key is not set
if openai.api_key is None:
    raise ValueError(
    '''
    [headline_generation] API key is not set. 
    Please set the OPENAI_API_KEY environment variable.
    '''
    )


# ---------------------------------------------------
# Model: ChatGPT-4o-Mini
# ---------------------------------------------------
def generate_headline_with_4o_mini(news_outlet, locale, make_fake, used_prompts_list = []):
    """ 
    ### Generate a news headline using the GPT-4o Mini model.
    #### Args:
    - news_outlet (str): The news outlet to emulate
    - locale (str): The locale to write the headline in
    - make_fake (bool): Flag indicating if the headline should be fake
    - used_prompts_list (list): List of prompts to avoid repeating
    #### Returns:
    - headline, detail
    """

    print("Generating headline with GPT-4o Mini model. For `{news_outlet}` in `{locale}` language. Is fake: `{make_fake}`")
    additional_prompt = ""
    if make_fake:
        additional_prompt = '''Write a fake news article headline. The headline should sound at least fairly realistic.
        The detail should be about what makes the headline fake. 
        '''
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
    
    locale_name = locale_codes_to_names_map[locale]
    response = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            # Primary prompt
            {"role": "system", "content": 
                '''
                    You are a journalist writing a news article's headline.
                    Just the headline, and a line of detail used to generate it is needed.
                    The headline should be 8-14 words long.
                    Don't include double quotes in the headline.
                    Write the headline one 1 line and the detail on the next line.
                    Don't repeat the headline in the detail.
                    Don't say "headline" or "detail" in the response.
                    Avoid leaving trailing white spaces.
                    Make the detail 1 short sentence. It should be a nuanced detail.
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
            {"role": "system", "content": f"Emulate the style of the {locale_name} news outlet: {news_outlet}."},
            # Locale to write in
            {"role": "system", "content": f"Write the article in {locale_name} language. Add in some nuanced details."},
            # Avoid repeating prompts
            {"role": "system", "content": f"Don't repeat from these prompts: {used_prompts_list}"},
            # Additional prompt
            {"role": "system", "content": 
                '''
                Avoid using slang or idiomatic expressions.
                Make sure the headline and detail and are all included in the response (on separate lines).
                '''
            }            
        ]
    )
    
    content = response.choices[0].message.content
    headline = content.split("\n")[0]
    detail = content.split("\n")[1]        
    print(f"""
    -----------------------------------
    ->>> Headline generation
    - Headline: {headline}
    - Detail: {detail}
    -----------------------------------
    """
    )

    return headline, detail
     
    