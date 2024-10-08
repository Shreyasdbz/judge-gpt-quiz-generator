'''
This is the translations module. It is used to translate text between different languages.
'''

from utils.locales import locale_codes_to_names_map

import azure_client

_client = azure_client.get_client()

def translate(text, text_type, source_locale, target_locale, news_outlet_style, model):
    """
    ### Translate text from one language to another using the specified model.
    #### Args:
    - text (str): The text to translate
    - text_type (str): If the text is one of [headline, content, detail]
    - source_locale (str): The original locale of the text
    - target_locale (str): The target locale to translate the text to
    - news_outlet_style (str): The style to emulate of news outlets
	- model (str): The model to use for generating the translation
    #### Returns
    - str: translated text.
    """
    print(f"Translating `{text_type}` from `{source_locale}` to `{target_locale}` using {model} model. Emulating news outlet style: `{news_outlet_style}` ")
    source_locale_name = locale_codes_to_names_map[source_locale]
    target_locale_name = locale_codes_to_names_map[target_locale]
    response = _client.complete(
        model=model,
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
