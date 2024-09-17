'''
Aricle dataclass to store information about a news article. 
'''

import random
import string
import json
from dataclasses import dataclass, field, asdict
from datetime import datetime


@dataclass
class Article:
    '''
    ### Article dataclass to store information about a news article.
    #### Attributes:
    - uid: str - Unique identifier for the article
    - created_at: datetime - Date and time when the article was created
    - headline: str - headline of the article
    - detail: str - Specific details about the article
    - content: str - Content of the article
    - is_fake: bool - Flag indicating if the article is fake
    - style_or_source: str - Style (if generated) or source (if real) of the article
    - origin_locale: str - Locale of the original article
    - headline_model_used: str - Model used for headline generation
    - content_model_used: str - Model used for content generation
    - translation_model_used: str - Model used for content translation
    - localized_headline_en: str - Localized headline in English
    - localized_detail_en: str - Localized detail in English
    - localized_content_en: str - Localized content in English
    - localized_headline_es: str - Localized headline in Spanish
    - localized_detail_es: str - Localized detail in Spanish
    - localized_content_es: str - Localized content in Spanish
    - localized_headline_fr: str - Localized headline in French
    - localized_detail_fr: str - Localized detail in French
    - localized_content_fr: str - Localized content in French
    - localized_headline_de: str - Localized headline in German
    - localized_detail_de: str - Localized detail in German
    - localized_content_de: str - Localized content in German
    '''
    uid: str = field(default_factory=lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=10)))
    created_at: datetime = field(default_factory=datetime.now)
    headline: str = ""
    detail: str = ""
    content: str = ""
    is_fake: bool = False
    style_or_source: str = ""
    origin_locale: str = ""
    headline_model_used: str = ""
    content_model_used: str = ""
    translation_model_used: str = ""
    localized_headline_en: str = ""
    localized_detail_en: str = ""
    localized_content_en: str = ""
    localized_headline_es: str = ""
    localized_detail_es: str = ""
    localized_content_es: str = ""
    localized_headline_fr: str = ""
    localized_detail_fr: str = ""
    localized_content_fr: str = ""
    localized_headline_de: str = ""
    localized_detail_de: str = ""
    localized_content_de: str = ""
    
    def to_dict(self):
      return asdict(self)

    def to_json(self):
      return json.dumps(self.to_dict(), indent=4)