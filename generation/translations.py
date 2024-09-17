'''
This is the translations module. It is used to translate text between different languages.
'''

import os
import openai


openai.api_key = os.getenv("JUDGE_GPT_OPENAI_API_KEY")
# Throw error if API key is not set
if openai.api_key is None:
    raise ValueError(
        '''
        [headline_generation] API key is not set. 
        Please set the OPENAI_API_KEY environment variable.
        '''
        )
  

def translate_text(text, source_locale, target_locale, news_outlet_style):
    """
    ### Translate text from one language to another.
    #### Args:
    - text (str): The text to translate
    - source_locale (str): The original locale of the text
    - target_locale (str): The target locale to translate the text to
    - news_outlet_style (str): The style to emulate of news outlets
    #### Returns
    - str: translated text.
    """
    print(
    f'''
    Translating text from `{source_locale}` to `{target_locale}`.
    Emulating news outlet style: `{news_outlet_style}`
    Text: `{text}`
    '''
    )