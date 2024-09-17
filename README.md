# Judge-GPT News Generator

## Overview

The **Judge-GPT News Generator** is a Python command-line application that generates localized fake news articles in four languages—English (en), Spanish (es), French (fr), and German (de). The app simulates news articles mimicking the writing styles of popular local news outlets using various Large Language Models (LLMs). Additionally, it supports building a database of real news articles by scraping trusted sources. This app is part of the broader **Judge-GPT** project, which helps assess user ability to detect fake or real news through a quiz-based interface.

## Features

- **Localized Fake News Generation**: Generate fake news articles in English, Spanish, French, and German.
- **Multi-Model Content Generation**: Utilizes different LLMs (e.g., GPT-4o-mini, Mistra, LLaMA-3) to generate headlines and article content.
- **Translation Across Locales**: Translates content between languages using GPT-4o or similar LLMs.
- **Real News Scraping**: Scrape real news articles to create a database for comparison and analysis.
- **Optimized Content Generation**: Supports faster content generation by using a variety of LLMs.
- **Integration with CosmosDB**: Articles, user profiles, and quiz responses are stored in Azure CosmosDB for MongoDB.

## Prerequisites

- **Python 3.8+**
- **Azure CosmosDB for MongoDB**: For article storage.
- **LLM APIs**: Ensure access to the LLM models you are using (e.g., GPT-4o-mini, Mistra, LLaMA-3).
- **BeautifulSoup, Requests**: For web scraping real news articles.

## Setup

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/Shreyasdbz/judge-gpt-quiz-fe
   cd judge-gpt-quiz-fe
   ```

2. **Install Dependencies**:
   You can install the required packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys (TODO)**:
   Create a `.env` file in the root directory and add your LLM API keys and other configuration variables:

   ```bash
   LLM_A_API_KEY=your_key_here
   LLM_B_API_KEY=your_key_here
   COSMOS_DB_CONNECTION_STRING=your_connection_string_here
   ```

4. **Setup CosmosDB**:
   Configure your Azure CosmosDB for MongoDB connection string and database schema. Ensure you have the required collections for storing articles, user profiles, and responses.

## Usage

1. **Generate Fake News Articles (CLI NOT Implemented)**:
   You can run the command to generate a set of localized fake news articles.

   ```bash
   python generate_fake_news.py --language en --num-articles 10
   ```

   - `--language`: The locale for generating the headlines and content (en, es, fr, de).
   - `--num-articles`: Number of fake articles to generate.

2. **Translate Articles (NOT Implemented)**:
   To translate an article from one language to another:

   ```bash
   python translate_article.py --article-id <id> --target-language es
   ```

3. **Scrape Real News (NOT Implemented)**:
   Use the scraping tool to fetch real news articles:

   ```bash
   python scrape_real_news.py --source-url https://example-news-site.com
   ```

4. **Store Articles in CosmosDB**:
   Store the generated or scraped articles in Azure CosmosDB:
   ```bash
   python store_articles.py
   ```

## Roadmap

- **Enhanced LLM Support**: Add more LLMs for content generation and improve the speed of article generation.
- **Better Scraping**: Integrate more news sources and support structured news scraping.
- **Fake News Detection**: Expand on the ability to analyze the quiz responses from different demographics in the Judge-GPT project.

## Contributing

If you’d like to contribute to the project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
