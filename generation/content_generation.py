'''
This is the article content generation module. It generates news headlines using various different models.
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


# ---------------------------------------------------
# Model: ChatGPT-4o
# ---------------------------------------------------
def generate_content_with_4o(origin_locale, style, headline, context, is_fake, fake_detail):
  """
  ### Generates article content using the GPT-4o model.
  #### Args:
  - origin_locale (str): The original locale of the article
  - style (str): The style to emulate of news outlets
  - headline (str): Generated headline
  - context (str): Expanded context for the headline
  - is_fake (bool): Flag indicating if the generated headline is fake
  - fake_detail (str): Detail about what makes the headline fake / real
  #### Returns:
  - Generated content: [str]
  """
  print(f"Generating content with GPT-4o model. For `{origin_locale}` in `{style}` style. Is fake: `{is_fake}`")
  locale_name = locale_codes_to_names_map[origin_locale]
  response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
      # Primary prompt
      {"role": "system", "content": 
      f'''{primary_prompt}
      '''
      },
      # Headline & context
      {"role": "user", "content": f"The article you'll be writing about is headlined: {headline}."},
      {"role": "user", "content": f"Here's the context for the article: {context}."},
      # Detail about fake / real
      {"role": "user", "content": f"What makes this content {'fake' if is_fake else 'real'} is: {fake_detail}"},
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
  

