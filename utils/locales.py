'''
Locale util module to handle locales and news outlets related data.
'''

supported_locales = ['en', 'es', 'fr', 'de']

locale_codes_to_names_map = {
  'en': 'English',
  'es': 'Spanish',
  'fr': 'French',
  'de': 'German',
}

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
  "Reuters",
  "Associated Press",
  "CNN",
  "BBC News",
  "Fox News",
  "MSNBC",
  "NPR",
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
  "20 Minutos",
  "EFE",
  "Europa Press",
  "RTVE",
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
  "France 24",
  "Agence France-Presse (AFP)",
  "BFMTV",
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
  "Tagesschau",
  "Deutsche Welle",
]
news_outlets_map = {
  'en': news_outlets_en,
  'es': news_outlets_es,
  'fr': news_outlets_fr,
  'de': news_outlets_de,
}