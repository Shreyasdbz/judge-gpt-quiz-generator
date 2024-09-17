from dataclasses import dataclass, field
import random
import string
from datetime import datetime
from typing import Optional

supported_locales = ['en', 'es', 'fr', 'de']

# New outlets by locale
news_outlets_en = [
  "The New York Times (NYT)",
  "The Washington Post",
  "The Guardian",
  "The Wall Street Journal",
  "USA Today",
  "Financial Times",
  "The Economist",
  "Bloomberg",
]
news_outlets_es = [
  "El País",
  "El Mundo",
  "La Vanguardia",
  "ABC",
  "El Confidencial",
  "La Razón",
  "El Español",
  "Público",
]
news_outlets_fr = [
  "Le Monde",
  "Le Figaro",
  "Libération",
  "L'Express",
  "Les Echos",
  "Le Parisien",
  "La Croix",
  "Marianne",
]
news_outlets_de = [
  "Bild",
  "Die Welt",
  "Frankfurter Allgemeine Zeitung",
  "Süddeutsche Zeitung",
  "Der Spiegel",
  "Die Zeit",
  "Handelsblatt",
  "Focus",
]
news_outlets_map = {
  'en': news_outlets_en,
  'es': news_outlets_es,
  'fr': news_outlets_fr,
  'de': news_outlets_de,
}

'''
Article dataclass to store information about a news article.
# Attributes:
#   uid: str - Unique identifier for the article
#   created_at: datetime - Date and time when the article was created
#   title: str - Title of the article
#   content: str - Content of the article
#   is_fake: bool - Flag indicating if the article is fake
#   style_or_source: str - Style (if generated) or source (if real) of the article
#   origin_locale: str - Locale of the original article
#   headline_generation_model_used: str - Model used for headline generation
#   headline_translation_model_used: str - Model used for headline translation
#   headline_context: str - Context for the headline that's generated which can be used to generate the content
#   content_model_used: str - Model used for content generation
#   content_translation_model_used: str - Model used for content translation
#   localized_title_en: str - Localized title in English
#   localized_content_en: str - Localized content in English
#   localized_title_es: str - Localized title in Spanish
#   localized_content_es: str - Localized content in Spanish
#   localized_title_fr: str - Localized title in French
#   localized_content_fr: str - Localized content in French
#   localized_title_de: str - Localized title in German
#   localized_content_de: str - Localized content in German
'''
@dataclass
class Article:
    uid: str = field(default_factory=lambda: ''.join(random.choices(string.ascii_letters + string.digits, k=10)))
    created_at: datetime = field(default_factory=datetime.now)
    title: str = ""
    content: str = ""
    is_fake: bool = False
    style_or_source: str = ""
    origin_locale: str = ""
    headline_generation_model_used: str = ""
    headline_translation_model_used: str = ""
    headline_context: str = ""
    content_model_used: str = ""
    content_translation_model_used: str = ""
    localized_title_en: str = ""
    localized_content_en: str = ""
    localized_title_es: str = ""
    localized_content_es: str = ""
    localized_title_fr: str = ""
    localized_content_fr: str = ""
    localized_title_de: str = ""
    localized_content_de: str = ""
