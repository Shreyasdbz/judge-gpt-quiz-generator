'''
This is the article content generation module. It generates news headlines using various different models.
'''

from utils.locales import locale_codes_to_names_map
import azure_client

_client = azure_client.get_client()


# Generic prompts for content generation
primary_prompt = '''
  You are a journalist writing a short news article that's roughly 50 - 75 words long.
  Don't say anything that could be considered very offensive or inappropriate.
  Don't say "content" or "article" in your response.
  Avoid leaving trailing whitespace at the end of your response.
  Avoid expressing what could be considered a personal opinion.
  Avoid repeating the same information in different ways.
  The output can be multiple lines, but avoid excessively long responses.
'''


def generate_content(origin_locale, style, headline, detail, is_fake, fake_detail, model):
  """
  ### Generates article content using the specified model.
  #### Args:
  - origin_locale (str): The original locale of the article
  - style (str): The style to emulate of news outlets
  - headline (str): Generated headline
  - detail (str): Some detail for the headline
  - is_fake (bool): Flag indicating if the generated headline is fake
  - fake_detail (str): Detail about what makes the headline fake / real
  - model (str): The model to use for generating the content
  #### Returns:
  - Generated content: [str]
  """
  print(f"Generating content with {model} model. For `{origin_locale}` in `{style}` style. Is fake: `{is_fake}`")
  locale_name = locale_codes_to_names_map[origin_locale]
  response = _client.complete(
    model=model,
    messages=[
      # Primary prompt
      {"role": "system", "content": 
      f'''{primary_prompt}
      '''
      },
      # Headline
      {"role": "user", "content": f"The article you'll be writing about is headlined: {headline}."},
      # Detail
      {"role": "user", "content": f"What makes this content {'fake' if is_fake else 'real'} is this detail: {detail}"},
      # Real or fake
      {"role": "user", "content": f"Keep in mind that the story you're writing is {'fake' if is_fake else 'real'}"},
      # Style
      {"role": "user", "content": f"Write this article in the style of the {locale_name} news outlet {style}."},
      # Locale
      {"role": "user", "content": f"Write this article in {locale_name} language."},
    ]
  )
  
  content = ""
  try:
    content = response.choices[0].message.content
  except:
      print(f"Failed to extract content from the response: {response}")
    
  print(f"""
  -----------------------------------
  ->>> Content generation
  - Content: 
  {content}
  -----------------------------------
  """
  )
  
  return content
  

