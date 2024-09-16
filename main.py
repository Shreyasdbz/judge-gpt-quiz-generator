'''
Project oveview:
This app generates news articles (and headlines) in various languages using different news
outlets styles via a combination of GPT-4o and various other LLMs. Each article is also
translated into all 4 supported languages.
News headline generation is handled by ChatGPT-4o and content generation is handled by the
respective LLMs. These include GPT-4, GPT-4o, Phi-3-medium-4k-instruct, Llama-2,
Meta-Llama-3.1, Mistral-large, etc.
'''

from headline_generation import generate_multiple_headlines

# def initialize():
#     """ Initialize the application """
#     print("Initializing application...")

# def process_data():
#     """ Process the data """
#     print("Processing data...")

# def cleanup():
#     """ Clean up the application """
#     print("Cleaning up...")

def main():
    """ main """
    
    generate_multiple_headlines(
        generate_limit=10,
        make_fake_choices=[True, False],
        locales_to_use=['en', 'es', 'fr', 'de'],
        generated_headlines_file_path="generated_headlines.json"
    )    

if __name__ == "__main__":
    main()
