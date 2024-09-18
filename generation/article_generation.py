import random
import json
from datetime import datetime
from typing import List

from classes.article import Article
from utils.locales import news_outlets_map, supported_locales
from utils.misc import generate_unique_id
from generation import content_generation
from generation import headline_generation
from generation import translations

ARTICLES_FILE_PATH = "data/generated_articles.json"
HEADLINE_FILE_PATH = "data/generated_headlines.json"


def generate_single_article(
    locale_choices: List[str],
    make_fake_choices: List[bool],
    used_prompts_list: List[str],
    model: str
    ):
    '''
    ### Pipeline for generating a single article. Does not store the generated article.
    1. Picks a random locale to use from the passed in options as well as a corresponding
        news outlet style to emulate.
    2. Uses {model} to generate a headline and a detail in the locale.
    3. Picks a random content model to use for generating the article.
    4. Generated headline and content are then translated into the rest of the supported locales.
    
    #### Args:
        locale_choices (list): List of locales to generate articles for
        make_fake_choices (list): [True, False] choices for generating fake articles or not
        used_prompts_list (list): List of used prompts to avoid repeating headlines
    #### Returns:
        Article object
    '''
    print(
        f'''
        Generating article.
        Headline model: {model}
        Locales: {locale_choices}
        Fake: {make_fake_choices}
        '''
    )    
    new_article: Article = Article()
    
    locale_to_use = random.choice(locale_choices)
    style_to_use = random.choice(news_outlets_map[locale_to_use])
    make_fake = random.choice(make_fake_choices)
    
    # Generate article headline
    headline, detail = headline_generation.generate_headline(
        news_outlet=style_to_use,
        locale=locale_to_use,
        make_fake=make_fake,
        used_prompts_list=used_prompts_list,
        model=model
    )
    new_article.uid = generate_unique_id()
    new_article.created_at = datetime.now().isoformat()
    new_article.origin_locale = locale_to_use
    new_article.style_or_source = style_to_use
    new_article.is_fake = make_fake
    new_article.detail = detail
    new_article.headline = headline
    new_article.headline_model_used = model
    
    # Generate article content
    # -- TODO: Based on the content model choice, pick the appropriate model
    content = content_generation.generate_content(
        origin_locale=locale_to_use,
        style=style_to_use,
        headline=headline,
        detail=detail,
        is_fake=make_fake,
        fake_detail=detail,
        model=model
    )
    new_article.content = content
    new_article.content_model_used = model
    
    # Translate headline and content into the rest of the supported locales
    new_article.translation_model_used = model
    # First, fill out the current locale's translations
    if locale_to_use == "en":
        new_article.localized_headline_en = headline
        new_article.localized_detail_en = detail
        new_article.localized_content_en = content
    elif locale_to_use == "es":
        new_article.localized_headline_es = headline
        new_article.localized_detail_es = detail
        new_article.localized_content_es = content
    elif locale_to_use == "fr":
        new_article.localized_headline_fr = headline
        new_article.localized_detail_fr = detail
        new_article.localized_content_fr = content
    elif locale_to_use == "de":
        new_article.localized_headline_de = headline
        new_article.localized_detail_de = detail
        new_article.localized_content_de = content
    # Now, the rest  
    languages_to_translate_into = [lang for lang in locale_choices if lang != locale_to_use]
    for lang in languages_to_translate_into:
        translated_headline = translations.translate(
            text=headline, 
            text_type="headline", 
            source_locale=locale_to_use, 
            target_locale=lang, 
            news_outlet_style=style_to_use,
            model=model
        )
        translated_detail = translations.translate(
            text=detail, 
            text_type="detail", 
            source_locale=locale_to_use, 
            target_locale=lang, 
            news_outlet_style=style_to_use,
            model=model
        )
        translated_content = translations.translate(
            text=content, 
            text_type="content", 
            source_locale=locale_to_use, 
            target_locale=lang, 
            news_outlet_style=style_to_use,
            model=model
        )
        if lang == "en":
            new_article.localized_headline_en = translated_headline
            new_article.localized_detail_en = translated_detail
            new_article.localized_content_en = translated_content
        elif lang == "es":
            new_article.localized_headline_es = translated_headline
            new_article.localized_detail_es = translated_detail
            new_article.localized_content_es = translated_content
        elif lang == "fr":
            new_article.localized_headline_fr = translated_headline
            new_article.localized_detail_fr = translated_detail
            new_article.localized_content_fr = translated_content
        elif lang == "de":
            new_article.localized_headline_de = translated_headline
            new_article.localized_detail_de = translated_detail
            new_article.localized_content_de = translated_content
    
    # Return the generated article object
    return new_article


def generate_and_store_single_article(model):
    '''
    #### Generates a single article and stores it in the generated_articles.json file.
    '''
    
    fetched_articles = []
    current_headlines:List[str] = []
    articles_to_add:List[Article] = []
    
    # Read in previously generated headlines via DB fetched headlines
    with open (HEADLINE_FILE_PATH, 'r') as read_file:
        data = json.load(read_file)
        fetched_headlines = data["headlines"]
        print(f"Retrieved {len(fetched_headlines)} headlines from file.")
        for i in range(len(fetched_headlines)):
            current_headlines.append(fetched_headlines[i])
        read_file.close()
    
    # Read in previously generated headlines via fresh articles 
    with open (ARTICLES_FILE_PATH, 'r') as read_file:
        data = json.load(read_file)
        fetched_articles = data["articles"]
        print(f"Retrieved {len(fetched_articles)} articles from file.")
        if(len(fetched_articles) > 0):
            for i in range(len(fetched_articles)):
                current_headlines.append(fetched_articles[i]["headline"])
        read_file.close()
        
    # Generate a single article
    new_article = generate_single_article(
        locale_choices=supported_locales,
        make_fake_choices=[True, False],
        used_prompts_list=current_headlines,
        model=model
    )
    articles_to_add.append(new_article)
    
    # Update generated_headlines.json file with the new headline
    headline_to_add = new_article.localized_headline_en
    with open(HEADLINE_FILE_PATH, 'w') as write_file:
        fetched_headlines.append(headline_to_add)
        json.dump({"headlines": fetched_headlines}, write_file, indent=4)
    
    # Write out to file
    with open(ARTICLES_FILE_PATH, 'w') as write_file:
        for article in articles_to_add:
            fetched_articles.append(article.to_dict())
        json.dump({"articles": fetched_articles}, write_file, indent=4)    
