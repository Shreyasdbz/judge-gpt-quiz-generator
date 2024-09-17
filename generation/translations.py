'''
This is the translations module. It is used to translate text between different languages.
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
  

def translate_text(text, text_type, source_locale, target_locale, news_outlet_style):
    """
    ### Translate text from one language to another.
    #### Args:
    - text (str): The text to translate
    - text_type (str): If the text is one of [headline, content, detail]
    - source_locale (str): The original locale of the text
    - target_locale (str): The target locale to translate the text to
    - news_outlet_style (str): The style to emulate of news outlets
    #### Returns
    - str: translated text.
    ### TODO:
    - Add support for more models.
    """
    print(
    f'''
    Translating text from `{source_locale}` to `{target_locale}`.
    Emulating news outlet style: `{news_outlet_style}`
    Text: `{text}`
    '''
    )
    
    translated_text = translate_using_gpt_35_turbo(text, text_type, source_locale, target_locale, news_outlet_style)
    return translated_text


# ------------------------------------
# GPT-3.5
# ------------------------------------
def translate_using_gpt_35_turbo(text, text_type, source_locale, target_locale, news_outlet_style):
    """
    ### Translate text from one language to another using the GPT-3.5 model.
    #### Args:
    - text (str): The text to translate
    - text_type (str): If the text is one of [headline, content, detail]
    - source_locale (str): The original locale of the text
    - target_locale (str): The target locale to translate the text to
    - news_outlet_style (str): The style to emulate of news outlets
    #### Returns
    - str: translated text.
    """
    print(f"Translating `{text_type}` from `{source_locale}` to `{target_locale}` using GPT-3.5 model. Emulating news outlet style: `{news_outlet_style}` ")
    source_locale_name = locale_codes_to_names_map[source_locale]
    target_locale_name = locale_codes_to_names_map[target_locale]
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            # Primary prompt
            {"role": "system", "content":
                '''
                You are a journalist translating a news article from one language to another.
                Retain the original meaning and style of the text.
                '''
            },
            # Text to translate
            {"role": "user", "content": f"The {text_type} you need to translate is: {text}."},
            # Source locale
            {"role": "user", "content": f"The original language of the text is: {source_locale_name}"},
            # Target locale
            {"role": "user", "content": f"Translate the text to: {target_locale_name}"},
            # Style
            {"role": "user", "content": f"When writing the text, try to emulate the style of {news_outlet_style} news outlet."},
            # Misc
            {"role": "user", "content": 
                '''
                Avoid using slang or idiomatic expressions.
                Avoid leaving trailing white spaces.
                Make sure to include nuances of the news outlet's style and source language.
                '''
            },
        ]
    )
    
    content = ""
    try:
        content = response.choices[0].message.content
    except:
        print(f"Failed to extract content from the response: {response}")

    print(f"""
    -----------------------------------
    ->>> Translation
    - Output: 
    {content}
    -----------------------------------
    """
    )

    return content
