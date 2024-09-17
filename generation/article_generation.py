
from datetime import datetime
import random
from typing import List

from classes.article import Article
from utils.locales import news_outlets_map
from utils.misc import generate_unique_id
from generation.content_generation import generate_content_with_4o
from generation.headline_generation import generate_headline_with_4o_mini


def generate_single_article(
    locale_choices: List[str],
    make_fake_choices: List[bool],
    content_model_choices: List[str],
    used_prompts_list: List[str]
):
    '''
    ### Pipeline for generating a single article. Does not store the generated article.
    1. Picks a random locale to use from the passed in options as well as a corresponding
        news outlet style to emulate.
    2. Uses GPT-4o-mini to generate a headline and a context in the locale.
    3. Picks a random content model to use for generating the article.
    4. Generated headline and content are then translated into the rest of the supported locales.
    
    #### Args:
        locale_choices (list): List of locales to generate articles for
        make_fake_choices (list): [True, False] choices for generating fake articles or not
        content_model_choices (list): List of content models to use for generating the article
        used_prompts_list (list): List of used prompts to avoid repeating headlines
    #### Returns:
        Article object
    '''
    print(
        f'''
        Generating article.
        Headline model: GPT-4o-mini
        Locales: {locale_choices}
        Fake: {make_fake_choices}
        Content models: {content_model_choices}
        '''
    )    
    new_article: Article = Article()
    
    locale_to_use = random.choice(locale_choices)
    style_to_use = random.choice(news_outlets_map[locale_to_use])
    make_fake = random.choice(make_fake_choices)
    
    # Generate article headline
    headline, context, detail = generate_headline_with_4o_mini(
        news_outlet=style_to_use,
        locale=locale_to_use,
        make_fake=make_fake,
        used_prompts_list=used_prompts_list
    )
    new_article.uid = generate_unique_id()
    new_article.created_at = datetime.now().isoformat()
    new_article.origin_locale = locale_to_use
    new_article.style_or_source = style_to_use
    new_article.is_fake = make_fake
    new_article.fake_details = detail
    new_article.title = headline
    new_article.headline_context = context
    new_article.headline_generation_model_used = "GPT-4o-mini"
    
    # Generate article content
    # -- Based on the content model choice, pick the appropriate model
    # -- TODO: Implement different models for content generation
    # -- For now, we are using GPT-4o for content generation
    content = generate_content_with_4o(
        origin_locale=locale_to_use,
        style=style_to_use,
        headline=headline,
        context=context,
        is_fake=make_fake,
        fake_detail=detail
    )
    new_article.content = content
    new_article.content_model_used = "GPT-4o"
    
    # Return the generated article object
    return new_article